from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Product, CustomerFeedBack


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']



class CreateProduct(ModelForm):
  class Meta:
        model = Product
        fields = ['name', 'price', 'image','available', 'discount']
        labels = {
          'name': '',
          'price': '',
          'image': '',
          'available': '',
          

        }
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Product Name'}),
            'price': forms.TextInput( attrs={'class': 'form-control', 'placeholder':'Product Price'}),
            'image': "",
            'available': forms.TextInput( attrs={'class': 'form-control', 'placeholder':'Product quantity'}),
            'discount':''

        }
    

class CustomerComment(ModelForm):
  class Meta:
        model = CustomerFeedBack
        fields = ['name','email','comment','paid']
        labels = {
          'name': '',
          'email': '',
          'comment': '',
          
          

        }
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name......'}),
            'email': forms.EmailInput( attrs={'class': 'form-control', 'placeholder':'Email......'}),
            'comment': forms.Textarea( attrs={'class': 'form-control', 'placeholder':'Enter text.....'}),
    

        }
    
