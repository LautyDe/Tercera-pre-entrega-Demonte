from django.urls import path
from ClothesShop.views import shoe_form, shirt_form, shoes, shirts, init, register

urlpatterns = [
    path('', init, name='Init'),
    path('shoes', shoes, name='Shoes'),
    path('add-shoe', shoe_form, name='Add-Shoe'),
    path('shirts', shirts, name='Shirts'),
    path('add-shirt', shirt_form, name='Add-shirt'),
    path('register', register, name='Register'),

    #path('search-category', search_category, name='Search_Category'),
    #path('search-curse', search_curse, name='Search_Curse'),
]
