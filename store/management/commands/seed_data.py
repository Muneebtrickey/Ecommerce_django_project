from django.core.management.base import BaseCommand
from store.models import Category, Product
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Populates the database with modern dummy categories and products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Cleaning existing data...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Define Categories
        categories_data = [
            {
                'name': 'Electronics',
                'description': 'Latest gadgets, smartphones, and high-performance computing.',
                'image_url': 'https://images.unsplash.com/photo-1498049794561-7780e7231661?auto=format&fit=crop&q=80&w=800',
            },
            {
                'name': 'Fashion',
                'description': 'Trendy apparel, designer wear, and premium accessories.',
                'image_url': 'https://images.unsplash.com/photo-1445205170230-053b83016050?auto=format&fit=crop&q=80&w=800',
            },
            {
                'name': 'Home & Decor',
                'description': 'Elegant furniture and modern interior design elements.',
                'image_url': 'https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&q=80&w=800',
            }
        ]

        # Define Products
        products_data = [
            # Electronics
            {
                'category': 'Electronics',
                'name': 'Premium Wireless Headphones',
                'small_description': 'Noise-cancelling, 40h battery life, premium sound.',
                'description': 'Experience studio-quality audio with our latest noise-cancelling wireless headphones. Designed for comfort and durability, these headphones offer up to 40 hours of playback on a single charge.',
                'original_price': 299.99,
                'selling_price': 249.00,
                'quantity': 50,
                'trending': True,
                'tag': 'New Arrival',
                'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&q=80&w=800'
            },
            {
                'category': 'Electronics',
                'name': 'Ultra-Slim Smartphone',
                'small_description': '6.7" OLED display, 5G ready, triple camera.',
                'description': 'The next generation of smartphones is here. Featuring a stunning 6.7-inch OLED display and a powerful triple-camera system for professional-grade photography.',
                'original_price': 999.00,
                'selling_price': 899.00,
                'quantity': 30,
                'trending': True,
                'tag': 'Best Seller',
                'image_url': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&q=80&w=800'
            },
            # Fashion
            {
                'category': 'Fashion',
                'name': 'Classic Leather Jacket',
                'small_description': 'Genuine lambskin leather, timeless design.',
                'description': 'A wardrobe essential. This classic leather jacket is crafted from 100% genuine lambskin leather and features a timeless silhouette that never goes out of style.',
                'original_price': 150.00,
                'selling_price': 120.00,
                'quantity': 25,
                'trending': True,
                'tag': 'Limited Edition',
                'image_url': 'https://images.unsplash.com/photo-1521223890158-f9f7c3d5d504?auto=format&fit=crop&q=80&w=800'
            },
            {
                'category': 'Fashion',
                'name': 'Minimalist Quartz Watch',
                'small_description': 'Stainless steel case, sapphire glass.',
                'description': 'Elegance in simplicity. This minimalist timepiece features a scratch-resistant sapphire crystal and a premium Italian leather strap.',
                'original_price': 199.00,
                'selling_price': 149.00,
                'quantity': 40,
                'trending': False,
                'tag': 'Classic',
                'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&q=80&w=800'
            },
            # Home & Decor
            {
                'category': 'Home & Decor',
                'name': 'Modern Velvet Armchair',
                'small_description': 'Ergonomic design, soft velvet upholstery.',
                'description': 'Add a touch of luxury to your living space with our modern velvet armchair. Featuring ergonomic support and high-density foam for ultimate comfort.',
                'original_price': 450.00,
                'selling_price': 399.00,
                'quantity': 15,
                'trending': True,
                'tag': 'Featured',
                'image_url': 'https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?auto=format&fit=crop&q=80&w=800'
            }
        ]

        # Create Categories
        created_categories = {}
        for cat in categories_data:
            obj = Category.objects.create(
                name=cat['name'],
                slug=slugify(cat['name']),
                description=cat['description'],
                status=False,
                trending=True,
                meta_title=cat['name'],
                meta_keywords=cat['name'],
                meta_description=cat['description']
            )
            # Since we can't easily upload images via script without local files, 
            # we'll rely on our template fallback to the Unsplash URL if no file exists.
            # However, for a better demo, I'll store the URL in a way the template can use.
            created_categories[cat['name']] = obj
            self.stdout.write(f'Created Category: {cat["name"]}')

        # Create Products
        for prod in products_data:
            Product.objects.create(
                category=created_categories[prod['category']],
                name=prod['name'],
                slug=slugify(prod['name']),
                small_description=prod['small_description'],
                description=prod['description'],
                original_price=prod['original_price'],
                selling_price=prod['selling_price'],
                quantity=prod['quantity'],
                status=False,
                trending=prod['trending'],
                tag=prod['tag'],
                meta_title=prod['name'],
                meta_keywords=prod['name'],
                meta_description=prod['small_description']
            )
            self.stdout.write(f'Created Product: {prod["name"]}')

        self.stdout.write(self.style.SUCCESS('Successfully populated dummy data!'))
        self.stdout.write(self.style.WARNING('Note: Images are using placeholder URLs in templates since local files were not uploaded.'))
