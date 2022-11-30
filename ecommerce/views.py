from django.shortcuts import render, redirect
from .models import Product,Order,OrderItem,ShippingAddress,User,CustomerFeedBack
from django.contrib import messages 
from django.http import JsonResponse
import json
import datetime
from .utils import CookieCart, CartData, GuestOrder
from .forms import UserRegisterForm, CreateProduct, CustomerComment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

#  INVENTORY
@login_required
def store(request):
    product = Product.objects.all()
    prod = len(product)

    order = Order.objects.filter(completed=True)
    order_len = len(order)

    customer = User.objects.all()
    cust = len(customer)
    
    context ={
        'products':product,
        'product':prod,
        'order':order_len,
        'customers':cust
    }
    return render(request, 'store/store.html', context)

# @login_required
def ordertable(request):
    order = OrderItem.objects.all()
    shipping = ShippingAddress.objects.all()
    context = {
        'orders':order,
        'shippings':shipping
    }
    return render(request, 'store/order_table.html', context)



# INVENTORY CRUD OPERATION
@login_required
def additems(request):
    if request.method != 'POST':
        form = CreateProduct()
    else:
        form = CreateProduct(request.POST , request.FILES )
        if form.is_valid():
            form.save()
            # messages.success(request,'New Product Added Successfully!!')
            return redirect('store')
        
    return render(request, 'store/addItem.html',{'form':form})



@login_required
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = CreateProduct(instance=product)
    
    if request.method =='POST':
        form = CreateProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            # messages.success(request,'Product Updated Successfully!!')
            return redirect('store')
    context = {
        'form':form
    }
    return render(request, 'store/updateItem.html', context)

@login_required
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('store')
    context = {'product':product}
    return render(request, 'store/deleteProduct.html', context)
    


@login_required
def deleteOrder(request, pk):
    order = OrderItem.objects.get(id=pk)
    order.delete()
    return redirect('order-table')
    pass

@login_required
def deleteShippingDetails(request, pk):
    shipping = ShippingAddress.objects.get(id=pk)
    shipping.delete()
    return redirect('order-table')

# def customerComment(request): 
#     if request.method == "POST":
#         form = CustomerComment(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('comment')
#     else:
#         form = CustomerComment()

#     return render(request, 'squad/message.html', {'form':form})
@login_required
def customerTable(request):
    customers = User.objects.all()

    return render(request, 'store/customers.html',{'customers':customers})


# INVENTORY ENDS HERE






#  ACCOUNT BEGINS HERE
@unauthenticated_user
def register(request):
    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully!!')
            return redirect('login')

    else: 
        messages.get_messages
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

def feedback(request):
    message = CustomerFeedBack.objects.all()
    context = {
        'messages':message
    }
    return render(request, 'store/message.html', context)

def customerComment(request): 
    if request.method == "POST":
        form = CustomerComment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment')
    else:
        form = CustomerComment()

    return render(request, 'squad/message.html', {'form':form})

@unauthenticated_user
def loginPage(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('livestock-market')
        else:
            messages.info(request,'Invalid Credentials!!!')

  
    return render(request, 'accounts/login.html')


def logoutUser(request):

    logout(request)
    return redirect('livestock-market')


def userPage(request):
    context = {}
    return render(request, 'accounts/user.html', context)
# ACCOUNT ENDS HERE







# ECOMMERCE BEGINS HERE
def livestock(request):
    data = CartData(request)
    cartItems = data['cartItems']
    product = Product.objects.all()
        
    context = {
        
        'cartItems':cartItems,
        'product':product,
    
    }
    return render(request, 'squad/livestock.html', context)


def cart(request):

    data = CartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'squad/cart.html', context)

def removeCart(request, pk):
    order = OrderItem.objects.get(id=pk)
    # if request.method == 'POST':
    order.delete()
    return redirect('cart')
    # context = {'order':order}
    # return render(request, 'squad/removeCart.html', context)

def viewItem(request, pk):
    data = CartData(request)
    cartItems = data['cartItems']
    product = Product.objects.get(id=pk)

    context = {'product':product, 'cartItems':cartItems}
    return render(request, 'squad/viewProduct.html', context)


def checkout(request):

    data = CartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'squad/checkout.html', context)



def UpdateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action  = data['action']
    print('Action:', action)
    print('Product', productId)

    customer = request.user
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer, completed=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)

    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete( )


    context = {}
    return JsonResponse('Item was added', safe=False)





def ProcessOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
    

    else:
        customer, order = GuestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id
        

    if total == total:
        order.completed =True
    order.save()

    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        mobile=data['shipping']['mobile'],
        zipcode=data['shipping']['zipcode'],
    )
    return JsonResponse('payment completed..', safe=False)

    # ECOMMERCE ENDS HERE




   
   
