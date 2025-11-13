from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('myaccount/', views.myaccount, name='myaccount'),
    path('my_store/', views.mystore, name='mystore'),
    path('my_store/add_product/', views.add_product, name='add_product'),
    path('my-store/order_detail/<int:pk>/', views.my_store_order_detail, name='my_store_order_detail'),
    path('my-store/edit-product/<int:pk>/', views.edit_product, name='edit_product'),
    path('my-store/delete-product/<int:pk>', views.delete_product, name='delete_product'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('vendor/<int:pk>/', views.vendor_detail, name='vendor_detail'),

]
