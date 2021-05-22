from django.contrib import admin
from django.urls import path
from home import views
from . import views
admin.site.site_header = "DADIDUE Admin"
admin.site.site_title = "DADIDUE Admin Portal"
admin.site.index_title = "Welcome to DADIDUE Portal"

urlpatterns = [
  

    path("home",views.index, name='home0'),
    path("login/",views.login, name='login'),
    path("logout/",views.login, name='logout'),
    path("about",views.about, name='about'),
    path("contact",views.contact, name='contact'),
    path("services",views.services, name='services'),
    path('products/', views.products,name="products"),
    path('customer/<str:pk_test>/', views.customer,name="customer"),
    path("",views.home,name="home"),
    path('create_order/', views.createOrder, name="create_order"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('registered/', views.registered,name="registered"),
    path('audio/', views.audio,name="audio"),
    path('creative/', views.creative,name="creative"),
    path('graphic/', views.graphic,name="graphic"),
    path('article/', views.article,name="article"),
    path('photo/', views.photo,name="photo"),
    path('video/', views.video,name="video"),
    path('logo/', views.logo,name="logo"),
    path('requested/', views.requested,name="requested"),
    path('freelancer/', views.freelancer,name="freelancer"),
    path('submitted/', views.submitted,name="submitted"),
   
]