from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import JsonResponse
from store.models import Product, Cart, WhishList
from django.contrib.auth.decorators import login_required 

@login_required(login_url="loginpage")
def index(request):
    """
    Renders the wishlist page for the authenticated user.
    """
    wishlist = WhishList.objects.filter(user=request.user)
    context = {'wishlist': wishlist}
    return render(request, "store/wishlist.html", context)


def addtowishlist(request):
    """
    Handles AJAX request to add a product to the user's wishlist.
    Validates user authentication and product existence.
    """
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.filter(id=prod_id).first()
            
            if product_check:
                if WhishList.objects.filter(user=request.user, product_id=prod_id).exists():
                    return JsonResponse({'status': "Product already in wishlist"})
                else:
                    WhishList.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status': "Product added to wishlist"})
            else:
                return JsonResponse({'status': "Product not found"})
        else:
            return JsonResponse({'status': "Login to continue"})
            
    return redirect("/")


def deletewishlistitem(request):
    """
    Handles AJAX request to remove an item from the wishlist.
    """
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))

            wishlistitem = WhishList.objects.filter(user=request.user, product_id=prod_id).first()
            if wishlistitem:
                wishlistitem.delete()
                return JsonResponse({'status': "Removed from wishlist"})
            else:
                return JsonResponse({'status': "Product not found in wishlist"})
        else:
            return JsonResponse({'status': "Login to continue"})

    return redirect("/")