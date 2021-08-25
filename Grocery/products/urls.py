from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    

    path('add/',views.additem,name="add_item"),
    path('all/',views.item_all,name="viewall_item"),
    path('update/<id>',views.update,name="update_item"),
    path('search/',views.search,name="search_item"),
    path('updateapi/',views.updateapi,name="update_item"),
    path('updatedata/',views.update_data,name="update_item"),
    path('deletedata/',views.delete_data,name="delete_item"),
    path('deleteapi/',views.deleteapi,name="delete_item"),

    path('',views.main,name="main_page"),
    path('add',views.addproducts,name="add_products"),
    path('all',views.view,name='view_all'),
    path('searchitem',views.search_page,name='search_product'),
    path('updateitem',views.update_page,name='update_product'),
    path('deleteitem',views.delete_page,name='Delete_product'),

]