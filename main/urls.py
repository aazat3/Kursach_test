from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', views.home, name='home'),
    path('overdue_order', views.overdue_order, name='overdue_order'),

    path('add_item', views.add_item, name='add_item'),
    path('add_rim', views.add_rim, name='add_rim'),
    path('add_lenses', views.add_lenses, name='add_lenses'),
    path('add_accessories', views.add_accessories, name='add_accessories'),

    path('customer', views.customer, name='customer'),
    path('shop_employee', views.shop_employee, name='shop_employee'),
    path('eye_doctor', views.eye_doctor, name='eye_doctor'),
    path('prescription', views.prescription, name='prescription'),
    path('create_prescription/<int:my_id>/', views.create_prescription, name='create_prescription'),
    path('order', views.order, name='order'),
    path('create_order/<int:my_id>/', views.create_order, name='create_order'),
    path('order_list_by_id_order/<int:my_id>/', views.order_list_by_id_order, name='order_list_by_id_order'),
    path('order_list_by_id_order_2/<int:my_id>/<int:id_catalog>/', views.order_list_by_id_order_2, name='order_list_by_id_order_2'),

    path('add_item_into_order_list/<int:my_id>/', views.add_item_into_order_list, name='add_item_into_order_list'),

    path('check/<int:my_id>/', views.check, name='check'),
    path('checkdowload/', views.checkdowload, name='checkdowload'),

    path('update_status1/<int:my_id>/', views.update_status1, name='update_status1'),
    path('update_status2/<int:my_id>/', views.update_status2, name='update_status2'),
    path('update_status3/<int:my_id>/', views.update_status3, name='update_status3'),
    path('update_quantity_rim/<int:my_id>/', views.update_quantity_rim, name='update_quantity_rim'),
    path('update_quantity_lenses/<int:my_id>/', views.update_quantity_lenses, name='update_quantity_lenses'),
    path('update_quantity_accessories/<int:my_id>/', views.update_quantity_accessories, name='update_quantity_accessories'),

    path('delete_prescription/<int:my_id>/', views.delete_prescription, name='delete_prescription'),
    path('delete_customer/<int:my_id>/', views.delete_customer, name='delete_customer'),
    path('delete_shop_employee/<int:my_id>/', views.delete_shop_employee, name='delete_shop_employee'),
    path('delete_eye_doctor/<int:my_id>/', views.delete_eye_doctor, name='delete_eye_doctor'),
    path('delete_lenses/<int:my_id>/', views.delete_lenses, name='delete_lenses'),
    path('delete_rim/<int:my_id>/', views.delete_rim, name='delete_rim'),
    path('delete_accessories/<int:my_id>/', views.delete_accessories, name='delete_accessories'),
    path('/<int:my_id>/delete_item/<int:item_id>/', views.delete_item, name='delete_item'),

    path('delete_order/<int:my_id>/', views.delete_order, name='delete_order'),
    #path('delete_confirm/<int:my_id>/', views.delete_confirm, name='delete_confirm'),

    path('last_prescription/<int:my_id>/', views.last_prescription, name='last_prescription'),


    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('profile/', views.profileemployee, name='profile'),

]