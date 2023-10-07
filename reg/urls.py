from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name= 'index'),
    path('signup/', views.signup, name= 'signup'),
    path('login/',views.login,name ='login'),
    path('logout/', views.logout,name='logout'),
    #path('',views.index,name = 'index'),
    #path('index/',views.index ,name = 'index'),
    #path('products/', views.product, name = 'products'),
     path('about/', views.about, name = 'about'),
     #path('client/', views.client, name = 'client'),
     path('contact/', views.contacts, name = 'contact')
    ]