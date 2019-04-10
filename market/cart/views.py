from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from supermarket.models import Category,Productdb
from django.views.decorators.csrf import csrf_protect
from .cart import Cart
from django.shortcuts import render
from .forms import CartAddProductForm
from django.core.mail import send_mail
from django.conf import settings

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Productdb, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Productdb, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart_detail.html', {'cart': cart})

def sendemail(request):
	print ("email sent")
	send_mail('hello','order recieved', settings.EMAIL_HOST_USER,['sayantikabanik122@gmail.com'],fail_silently=False)
#	return redirect('cart:cart_detail')
@csrf_protect
def login(request):
     csrfContext = RequestContext(request)
     return render_to_response('cart_detail.html', csrfContext)
