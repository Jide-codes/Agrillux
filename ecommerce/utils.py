import json
from .models import ShippingAddress, Product, Order, OrderItem, User

def CookieCart(request):

    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    print('Cart:', cart)
    items = []
    order = {'get_cart_total':0, 'get_cart_item':0}
    cartItems = order['get_cart_item']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_item'] += cart[i]['quantity']


            item = {
                'product':{
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'ImageURL':product.ImageURL
                },

                'quantity':cart[i]['quantity'],
                'get_total':total,
            }
            items.append(item)
        except:
            pass
    return{'cartItems':cartItems, 'order':order, 'items':items}



def CartData(request):

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item

    else:
        CookieData = CookieCart(request)
        cartItems = CookieData['cartItems']
        order = CookieData['order']
        items = CookieData['items']
    return{'cartItems':cartItems, 'order':order, 'items':items}


def GuestOrder(request, data):
    print('User is not logged in ....')

    print('COOKIES:', request.COOKIES)
    name = data['form']['username']
    email = data['form']['email']

    cookieData = CookieCart(request)
    items = cookieData['items']
    customer = request.user
    customer, created = User.objects.get_or_create(
            username=name,
            email= email
        )
    customer.name = name
    customer.save()

    order = Order.objects.create(
            customer = customer,
            completed = False
        )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )




    return customer, order
