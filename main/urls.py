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

    path('customer', views.customer, name='customer'),
    path('shop_employee', views.shop_employee, name='shop_employee'),
    path('eye_doctor', views.eye_doctor, name='eye_doctor'),
    path('prescription', views.prescription, name='prescription'),
    path('order', views.order, name='order'),
    path('order_list_by_id_order/<int:my_id>/', views.order_list_by_id_order, name='order_list_by_id_order'),

    path('update_status1/<int:my_id>/', views.update_status1, name='update_status1'),
    path('update_status2/<int:my_id>/', views.update_status2, name='update_status2'),
    path('update_status3/<int:my_id>/', views.update_status3, name='update_status3'),
    path('update_quantity_rim/<int:my_id>/', views.update_quantity_rim, name='update_quantity_rim'),
    path('update_quantity_lenses/<int:my_id>/', views.update_quantity_lenses, name='update_quantity_lenses'),
    path('update_quantity_accessories/<int:my_id>/', views.update_quantity_accessories, name='update_quantity_accessories'),

    path('delete_prescription/<int:my_id>/', views.delete_prescription, name='delete_prescription'),
    path('delete_order/<int:my_id>/', views.delete_order, name='delete_order'),
    #path('delete_confirm/<int:my_id>/', views.delete_confirm, name='delete_confirm'),

]