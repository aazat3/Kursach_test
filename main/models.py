from django.db import models

# Create your models here.


class MyId(models.Model):
    my_id = models.IntegerField()


class Accessories(models.Model):
    id_accessories = models.AutoField(primary_key=True)
    manufact = models.CharField(max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    type = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    price = models.FloatField()
    name_accessories = models.CharField(max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accessories'


class Color(models.Model):
    id_color = models.AutoField(primary_key=True)
    name_color = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'color'


class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    surname = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    phone_number = models.CharField(unique=True, max_length=12, db_collation='Cyrillic_General_CI_AS')
    email = models.CharField(unique=True, max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class EyeDoctor(models.Model):
    id_employee = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    surname = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    patronymic = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    post = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    phone_number = models.CharField(unique=True, max_length=12, db_collation='Cyrillic_General_CI_AS')
    passport_details = models.CharField(unique=True, max_length=50, db_collation='Cyrillic_General_CI_AS')
    adress = models.CharField(max_length=60, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eye_doctor'


class Lenses(models.Model):
    id_lenses = models.AutoField(primary_key=True)
    diopter = models.DecimalField(max_digits=4, decimal_places=2)
    id_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='id_color', blank=True, null=True)
    manufact = models.CharField(max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    price = models.FloatField()
    name_lenses = models.CharField(max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lenses'


class Prescription(models.Model):
    id_prescribtion = models.AutoField(primary_key=True)
    id_employee = models.ForeignKey(EyeDoctor, models.DO_NOTHING, db_column='id_employee', blank=True, null=True)
    id_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='id_customer', blank=True, null=True)
    right_diopter = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    left_diopter = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    distance = models.SmallIntegerField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'prescription'


class PrescriptionWithoutId(models.Model):
    id_prescribtion = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    employee_surname = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    customer_name = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    customer_surname = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    right_diopter = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    left_diopter = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    distance = models.SmallIntegerField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'prescription_without_id'


class Rim(models.Model):
    id_rim = models.AutoField(primary_key=True)
    id_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='id_color', blank=True, null=True)
    manufact = models.CharField(max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    price = models.FloatField()
    name_rim = models.CharField(max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rim'


class ShopEmployee(models.Model):
    id_employee = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    surname = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    patronymic = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    post = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    phone_number = models.CharField(unique=True, max_length=12, db_collation='Cyrillic_General_CI_AS')
    passport_details = models.CharField(unique=True, max_length=50, db_collation='Cyrillic_General_CI_AS')
    adress = models.CharField(max_length=60, db_collation='Cyrillic_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'shop_employee'


class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    meaning_status = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'status'


class Catalog(models.Model):
    id_catalog = models.AutoField(primary_key=True)
    id_lenses = models.OneToOneField(Lenses, models.DO_NOTHING, db_column='id_lenses', blank=True, null=True)
    id_rim = models.OneToOneField(Rim, models.DO_NOTHING, db_column='id_rim', blank=True, null=True)
    id_accessories = models.OneToOneField(Accessories, models.DO_NOTHING, db_column='id_accessories', blank=True, null=True)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog'


class Orderr(models.Model):
    id_order = models.AutoField(primary_key=True)
    id_employee = models.ForeignKey(ShopEmployee, models.DO_NOTHING, db_column='id_employee', blank=True, null=True)
    id_prescription = models.ForeignKey(Prescription, models.DO_NOTHING, db_column='id_prescription', blank=True, null=True)
    date_acceptance = models.DateTimeField()
    date_assignment = models.DateTimeField(blank=True, null=True)
    id_status = models.ForeignKey(Status, models.DO_NOTHING, db_column='id_status', blank=True, null=True)
    end_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'orderr'


class OrderrWithoutId(models.Model):
    id_order = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    employee_surname = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    customer_name = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    customer_surname = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    date_acceptance = models.DateTimeField()
    date_assignment = models.DateTimeField(blank=True, null=True)
    id_status = models.ForeignKey(Status, models.DO_NOTHING, db_column='id_status', blank=True, null=True)
    end_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Orderr_without_id'

class OrderList(models.Model):
    id_order_list = models.AutoField(primary_key=True)
    id_catalog = models.ForeignKey(Catalog, models.DO_NOTHING, db_column='id_catalog', blank=True, null=True)
    id_order = models.ForeignKey(Orderr, models.DO_NOTHING, db_column='id_order', blank=True, null=True)
    quantity = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_list'


class OrderListByIdOrder(models.Model):
    id_order_list = models.AutoField(primary_key=True)
    id_order = models.ForeignKey(Orderr, models.DO_NOTHING, db_column='id_order', blank=True, null=True)
    name = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    surname = models.CharField(max_length=20, db_collation='Cyrillic_General_CI_AS')
    id_catalog = models.ForeignKey(Catalog, models.DO_NOTHING, db_column='id_catalog', blank=True, null=True)
    product_name = models.CharField(max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    product_manufact = models.CharField(max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    quantity = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'order_list_by_id_order'


class OverdueOrder(models.Model):
    id_order = models.AutoField(primary_key=True)
    id_employee = models.ForeignKey(ShopEmployee, models.DO_NOTHING, db_column='id_employee', blank=True, null=True)
    date_acceptance = models.DateTimeField()
    id_status = models.ForeignKey(Status, models.DO_NOTHING, db_column='id_status', blank=True, null=True)
    end_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'overdue_order'
