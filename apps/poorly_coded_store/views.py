from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    context = {
        'orders': request.session['qt'],
        'price': request.session['pr'],
        'total': request.session['tp']
    }
    return render(request, 'store/checkout.html', context)

def purchase(request):
    my_price = Product.objects.get(id=request.POST['price'])
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float( my_price.price)
    total_charge = quantity_from_form * price_from_form
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)


    request.session['qt'] = quantity_from_form
    request.session['pr'] =   price_from_form
    request.session['tp'] = total_charge
    return redirect('checkout')
