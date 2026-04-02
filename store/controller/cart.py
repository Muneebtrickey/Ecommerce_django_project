from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import JsonResponse
from store.models import Product, Cart
from django.contrib.auth.decorators import login_required

def addtocart(request):
    """
    Handles AJAX request to add a product to the user's cart.
    Validates product existence, stock availability, and authentication.
    """
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'status': "Login to continue"})

        prod_id = int(request.POST.get('product_id'))
        product_check = Product.objects.filter(id=prod_id).first()
        
        if product_check:
            if Cart.objects.filter(user=request.user, product_id=prod_id).exists():
                return JsonResponse({'status': "Product already in cart"})
            else:
                prod_qty = int(request.POST.get('product_qty'))

                if product_check.quantity >= prod_qty:
                    Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                    return JsonResponse({'status': "Product added successfully"})
                else:
                    return JsonResponse({'status': f"Only {product_check.quantity} quantity available"})
        else:
            return JsonResponse({'status': "No such product found"})
    
    return redirect("/")

@login_required(login_url="loginpage")
def viewcart(request):
    """
    Renders the shopping cart page for the logged-in user.
    """
    cart = Cart.objects.filter(user=request.user)
    context = {'cart': cart}
    return render(request, "store/cart.html", context)


def updatecart(request):
    """
    Handles AJAX request to update the quantity of a product in the cart.
    """
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if Cart.objects.filter(user=request.user, product_id=prod_id).exists():
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status': "Updated successfully"})
    return redirect("/")


def deletecartitem(request):
    """
    Handles AJAX request to remove an item from the cart.
    """
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if Cart.objects.filter(user=request.user, product_id=prod_id).exists():
            cartitem = Cart.objects.get(product_id=prod_id, user=request.user)
            cartitem.delete()
            return JsonResponse({'status': 'Deleted successfully'})
    return redirect("/")