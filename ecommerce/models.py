from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Customer(models.Model):
#     user        = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     name        = models.CharField(max_length=200, null=True)
#     email       = models.EmailField(max_length=200, null=True)
    



    # def __str__(self):
    #     return self.name
    



class Product(models.Model):
    name        = models.CharField(max_length=200, null=True)
    price       = models.FloatField()
    image       = models.ImageField(upload_to = "media/")
    available   = models.CharField(max_length=200, null=False)
    discount    = models.BooleanField(default=False)
    
    

    def __str__(self):
        return self.name


    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
    
        return url



    @property
    def get_discount_price(self):
        if self.discount:
            discount_price = (90/100) * self.price
            return discount_price

        else: 
            return self.price

    @property
    def get_price(self):
        price = self.price
        return price



class Order(models.Model):
    customer        = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True )
    date_ordered    = models.DateTimeField(auto_now_add=True)
    completed       = models.BooleanField(default=False, null=True, blank=False)
    transaction_id  = models.CharField(max_length=200, null=True)
    
    


    def __str__(self):
        return f'{self.transaction_id}'


    def get_cart_total(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitem])
        return float(total)


    def get_cart_item(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitem])
        return total

class OrderItem(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order       = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity    = models.IntegerField(default=0, null=True, blank=True)
    date_added  = models.DateTimeField(auto_now_add=True)


    @property
    def get_total(self):
        if self.product.discount:
            total = self.product.get_discount_price * self.quantity
            return total
        else:
            total = self.product.price * self.quantity
            return total

    @property
    def get_price(self):
        price = self.product.price
        return price

    def __str__(self):
        return f'{self.product}'




class ShippingAddress(models.Model):
    customer        = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True )
    order           = models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True, null=True )
    address         = models.CharField(max_length=200, null=True)
    city            = models.CharField(max_length=200, null=True)
    state           = models.CharField(max_length=200, null=True)
    zipcode         = models.CharField(max_length=200, null=True)
    mobile          = models.CharField(max_length=200, null=True)
    date_added      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer}s shipping details'




class CustomerFeedBack(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    comment = models.TextField(max_length=100000, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name

