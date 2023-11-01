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

    path('create_customer', views.create_customer, name='create_customer'),
    path('create_shop_employee', views.create_shop_employee, name='create_shop_employee'),
    path('create_eye_doctor', views.create_eye_doctor, name='create_eye_doctor'),
    path('create_prescription', views.create_prescription, name='create_prescription'),
    path('create_order', views.create_order, name='create_order'),

    path('viewing_customers', views.viewing_customers, name='viewing_customers'),

    path('update_catalog', views.update_catalog, name='update_catalog'),

]