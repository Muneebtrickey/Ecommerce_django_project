from django.shortcuts import render, redirect
from .models import Category, Product
from django.contrib import messages

# Create your views here.

def home(request):
    """
    Renders the homepage with trending products and categories.
    """
    trending_products = Product.objects.filter(trending=1, status=0)[:8]
    trending_categories = Category.objects.filter(trending=1, status=0)
    context = {
        'trending_products': trending_products,
        'trending_categories': trending_categories
    }
    return render(request, "store/index.html", context)


def collections(request):
    """
    Renders all available (non-hidden) categories.
    """
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, "store/collections.html", context)

def collectionsview(request, slug):
    """
    Renders products within a specific category identified by its slug.
    """
    if Category.objects.filter(slug=slug, status=0).exists():
        products = Product.objects.filter(category__slug=slug, status=0)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category': category}
        return render(request, "store/product/index.html", context)
    else:
        messages.warning(request, "No such category found.")
        return redirect('collections')

def productview(request, cate_slug, prod_slug):
    """
    Renders the detail view of a specific product.
    Corrected: Added () to .first() and improved validation logic.
    """
    if Category.objects.filter(slug=cate_slug, status=0).exists():
        if Product.objects.filter(slug=prod_slug, status=0).exists():
            product = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'products': product} # Keeping 'products' as key for template compatibility, though singular
            return render(request, "store/product/view.html", context)
        else:
            messages.error(request, "No such product found.")
            return redirect('collections')
    else:
        messages.error(request, "No such category found.")
        return redirect('collections')