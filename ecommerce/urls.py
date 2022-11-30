from django.urls import path
from . import views

urlpatterns = [


   

        #  THE INVENTORY
    path('store/', views.store, name='store'),
    path('Order/', views.ordertable, name='order-table'),
    path('addItems/', views.additems, name='add-items'),
    path('update_product/<str:pk>/', views.updateProduct, name='update_product'),
    path('delete_product/<str:pk>/', views.deleteProduct, name='delete_product'),
    path('delete_OrderItem/<str:pk>/', views.deleteOrder, name='delete_OrderItem'),
    path('delete_shippingDetails/<str:pk>/', views.deleteShippingDetails, name='delete_shippingDetails'),
    path('Comment/', views.customerComment, name='comment'),
    path('CustomersTable/', views.customerTable, name='customers'),
    path('user/', views.userPage, name='user-page'),
    path('feedback/', views.feedback, name='feed_back'),


    # ACCOUNTS
    path('sign-up/',views.register, name='sign-up'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout-User'),
    
    
    # ECOMMERCE
    path('', views.livestock, name='livestock-market'),
    path('cart/', views.cart, name='cart'),
    path('remove/<str:pk>/', views.removeCart, name='remove-order'),
    path('view/<str:pk>/', views.viewItem, name='view-item'),
    path('checkout/', views.checkout, name='checkout'),


    #  THE JAVASCRIPT/DJANGO BACKEND LOGIC
    path('UpdateItem/', views.UpdateItem, name='UpdateItem'),
    path('ProcessOrder/', views.ProcessOrder, name='ProcessOrder'),



]
