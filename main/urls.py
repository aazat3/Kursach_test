from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('overdue_order', views.overdue_order, name='overdue_order'),

    path('add_item', views.add_item, name='add_item'),
    path('add_rim', views.add_rim, name='add_rim'),
    path('add_lenses', views.add_lenses, name='add_lenses'),
    path('add_accessories', views.add_accessories, name='add_accessories'),
    path('add_item_order', views.add_item_order, name='add_item_order'),

    path('customer', views.customer, name='customer'),
    path('shop_employee', views.shop_employee, name='shop_employee'),
    path('eye_doctor', views.eye_doctor, name='eye_doctor'),
    path('prescription', views.prescription, name='prescription'),
    path('order', views.order, name='order'),

    path('order_list_by_id_order/<int:my_id>/', views.order_list_by_id_order, name='order_list_by_id_order'),
    path('delete_prescription/<int:my_id>/', views.delete_prescription, name='delete_prescription'),

    path('update_catalog', views.update_catalog, name='update_catalog'),

]