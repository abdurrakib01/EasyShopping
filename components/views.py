from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Customer, Cart, OrderPlaced
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category = 'TW')
        bottomwears = Product.objects.filter(category = 'BW')
        mobile = Product.objects.filter(category = 'M')
        laptop = Product.objects.filter(category = 'L')
        context = {
            "topwears" : topwears,
            "bottomwears" : bottomwears,
            'mobile' : mobile,
            'laptop' : laptop
        }
        return render(request, 'comp/home.html', context)

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        product_exit = False
        if request.user.is_authenticated:
            product_exit = Cart.objects.filter(Q(product=pk)&Q(user=request.user)).exists()
        context = {
            'product':product,
            'product_exit' : product_exit
        }
        return render(request, 'comp/detail.html', context)

class MobileView(View):
    def get(self, request, data=None):
        if(data==None):
           mobile = Product.objects.filter(category='M')
        elif(data=='Apple' or data=='Samsung'):
            mobile = Product.objects.filter(category='M').filter(brand=data)
        context = {
            'mobile' : mobile,
        }
        return render(request, 'comp/mobile.html', context)

@method_decorator(login_required, name="dispatch")
class AddToCartView(View):
    def get(self, request):
        user = request.user
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(pk=product_id)
        Cart(user=user, product=product).save()
        return redirect('/carts/')

@method_decorator(login_required, name="dispatch")
class ShowCartsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            carts = Cart.objects.filter(user=user)
            amount = 0.0
            shipping_cost = 0.0
            total_amount = 0.0
            message = ""
            cart_products = [prod for prod in Cart.objects.all() if prod.user == user]
            if cart_products:
                for prod in cart_products:
                    amount += prod.product.selling_price*prod.quantity
                shipping_cost += 80.0
            else:
                message += "You have no product in your cart"
            total_amount += amount+shipping_cost
            context = {
                'carts':carts,
                'amount':amount,
                'shipping_cost':shipping_cost,
                'total_amount':total_amount,
                'message':message,
            }
        return render(request, 'comp/addtocart.html', context)

@login_required
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_cost = 0.0
        total_amount = 0.0
        cart_products = [prod for prod in Cart.objects.all() if prod.user == request.user]
        if cart_products:
            for prod in cart_products:
                amount += prod.product.selling_price*prod.quantity
            shipping_cost += 80.0
        total_amount += amount+shipping_cost
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'total_amount':total_amount
        }
        return JsonResponse(data)

@login_required
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        if(c.quantity > 1):
            c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_cost = 0.0
        total_amount = 0.0
        cart_products = [prod for prod in Cart.objects.all() if prod.user == request.user]
        if cart_products:
            for prod in cart_products:
                amount += prod.product.selling_price*prod.quantity
            shipping_cost += 80.0
        total_amount += amount+shipping_cost
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'total_amount':total_amount
        }
        return JsonResponse(data)

@login_required
def delete_cart(request):
    if request.method == 'GET':
        cart_id = request.GET.get("cart_id")
        print(cart_id)
        c = Cart.objects.get(Q(id = cart_id) & Q(user = request.user))
        c.delete()
    return redirect("/carts/")

@login_required       
def buy_now(request):
    if request.method == 'GET': 
        prod_id = request.GET.get("prod_id")
        product = Product.objects.get(pk=prod_id)
        amount = product.selling_price
        shipping_cost = 80.0
        total_amount = amount + shipping_cost
        customers = Customer.objects.filter(user=request.user)
        context = {
            'product':product,
            'amount' : amount,
            'customers':customers,
            'shipping_cost' : shipping_cost,
            'total_amount' : total_amount,
        }
        return render(request, 'comp/buy.html', context)

@login_required
def checkout_view(request):
    user = request.user
    carts = Cart.objects.filter(user=user)
    customers = Customer.objects.filter(user=user)
    amount = 0.0
    shipping_cost = 0.0
    total_amount = 0.0
    if carts:
        for prod in carts:
            amount += prod.product.selling_price*prod.quantity
        shipping_cost += 80.0
    total_amount += amount+shipping_cost
    context = {
        'carts':carts,
        'customers' : customers,
        'amount':amount,
        'shipping_cost':shipping_cost,
        'total_amount':total_amount,
    }
    return render(request, 'comp/checkout.html', context)

@login_required
def order_done(request):
    cusid = request.GET["customer"]
    customer = Customer.objects.get(pk=cusid)
    user = request.user
    carts = Cart.objects.filter(user=user)
    for cart in carts:
        order = OrderPlaced(user=user, customer=customer, product=cart.product, quantity=cart.quantity)
        order.save()
        carts.delete()
    return redirect("components:order")

@login_required
def order(request):
    user = request.user
    products = OrderPlaced.objects.filter(user = user)
    message = ""
    if not products:
        message += "You don't order any product yet"
    context = {
        'carts' : products,
        'message' : message,
    }
    return render(request, 'comp/orderdone.html', context)

@login_required
def orderplaced(request):
    prod_id = request.GET["prod_id"]
    cust_id = request.GET["customer"]
    product = Product.objects.get(pk=prod_id)
    customer = Customer.objects.get(pk=cust_id)
    user = request.user
    OrderPlaced(user=user, customer=customer, product=product, quantity=1).save()
    return redirect("components:order")

def laptop_list(request, data=None):
    if(data==None):
        laptops = Product.objects.filter(category='L')
    else:
        laptops = Product.objects.filter(category='L').filter(brand=data)
    return render(request, "comp/laptop.html", {"laptops":laptops})

def top_wear(request, data=None):
    if(data==None):
        fashion = Product.objects.filter(category="TW")
    else:
        fashion = Product.objects.filter(category="TW").filter(brand=data)
    return render(request, "comp/topwear.html", {"fashion":fashion})

def bottom_wear(request, data=None):
    if(data==None):
        fashion = Product.objects.filter(category="BW")
    else:
        fashion = Product.objects.filter(category="BW").filter(brand=data)
    return render(request, 'comp/bottomwear.html', {"fashion":fashion})