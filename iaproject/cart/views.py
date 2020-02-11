import stripe
from django.shortcuts import render, redirect
from django.contrib import messages
from iaproject.settings import STRIPE_PUBLISHABLE, STRIPE_SECRET
from portfolio.models import Download
from .models import Cart


# Create your views here.
# Credit: Coding Point https://www.youtube.com/watch?v=5q3c3kYSRzk&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK&index=23

def cart(request):
    try:
        current_cart_id = request.session['cart_id']
        cart = Cart.objects.get(pk=current_cart_id)
    except: 
        current_cart_id = None 
        cart = None
        messages.error(request, f'A cart has not been created.')
    context = {'title': 'Cart', 'cart': cart}
    return render(request, 'cart/cart.html', context)

def add(request, pk): #make cart for first time when add
    try: #checking to see if theres a cart id in session already
        current_cart_id = request.session['cart_id'] #request has a session attribute with key value pairs
    except: #if not create it
        new_cart = Cart()# new instance of model
        new_cart.save()
        request.session['cart_id'] = new_cart.id #create
        current_cart_id = request.session['cart_id']

    cart = Cart.objects.get(pk=current_cart_id)    
    download = Download.objects.get(pk=pk)
    project = download.project.id
    if not download in cart.downloads.all():
        cart.downloads.add(download)
        new_total = 0.00
        for download in cart.downloads.all():
            new_total += float(download.price)
        cart.total = new_total
        cart.save()
        request.session['download_count'] = cart.downloads.count() 
        messages.success(request, f'{download.title} added to cart.')
    else: 
        messages.warning(request, f'{download.title} already in cart.')
    return redirect('project', pk=project)   #don't need reverse... i think built in... request throws an error
# after u add to cart where do u want to go?


def remove(request, pk):
    try: #checking to see if theres a cart id in session already
        current_cart_id = request.session['cart_id'] #request has a session attribute with key value pairs
    except: #if not create it
        new_cart = Cart()# new instance of model
        new_cart.save()
        request.session['cart_id'] = new_cart.id #create
        current_cart_id = request.session['cart_id']

    cart = Cart.objects.get(pk=current_cart_id)    
    download = Download.objects.get(pk=pk)
    if download in cart.downloads.all():
        cart.downloads.remove(download)
        new_total = 0.00
        for download in cart.downloads.all():
            new_total += float(download.price)
        cart.total = new_total
        cart.save()
        request.session['download_count'] = cart.downloads.count() #create
        messages.success(request, f'{download.title} removed from cart.')
    #else:
        #messages.success(request, f'Download not in cart.')  
    return redirect('cart')   #do i need reverse????          


def charge(request):
    current_cart_id = request.session['cart_id']
    cart = Cart.objects.get(pk=current_cart_id)
    items = []
    for download in cart.downloads.all():
        item = {'name': download.title, 'description': download.content, 'amount': int((download.price)*100), 'currency': 'eur', 'quantity': 1}
        items.append(item)
    stripe.api_key = STRIPE_SECRET
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        success_url='http://127.0.0.1:8000/cart/success?session_id={CHECKOUT_SESSION_ID}',
        #success_url=request.build_absolute_uri('/cart/success?session_id={CHECKOUT_SESSION_ID}'),
        cancel_url=request.build_absolute_uri('/cart'),
        client_reference_id='A0'+str(cart.id)
        )
    context = {'sid': session.id,}
    
    return render(request, 'cart/charge.html', context)


def success(request):
    stripe_session = request.GET.get('session_id')
    stripe_data = stripe.checkout.Session.retrieve(stripe_session)

    cart_id = request.session['cart_id']
    cart = Cart.objects.get(pk=cart_id)
    cart.stripe = stripe_session
    cart.save()
    del request.session['cart_id']
    
    context = {'title': 'Purchase Complete', 'stripe_data': stripe_data, }
    return render(request, 'cart/success.html', context)
    #https://stackoverflow.com/questions/150505/capturing-url-parameters-in-request-get
    #https://stackoverflow.com/questions/16039399/how-to-clear-all-session-variables-without-getting-logged-out