from django.shortcuts import render, redirect
from django.db import connection
from .models import Accessories, Catalog, Color, Customer, EyeDoctor, Lenses, OrderList, Orderr, Prescription, Rim, ShopEmployee, Status, OverdueOrder
# Create your views here.


def home(request):
    rim = Rim.objects.all()
    lenses = Lenses.objects.all()
    accessories = Accessories.objects.all()
    return render(request, 'main/home.html', {'title': 'Главная страница сайта', 'rim': rim, 'lenses': lenses, 'accessories': accessories})


def about_us(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM hello_person WHERE name = 'Tomas'")
        row = cursor.fetchone()  # получаем одну строку
    return render(request, 'main/overdue_order.html')


def add_item(request):
    return render(request, 'main/add_item.html')


def add_rim(request):
    if request.method == "POST":
        name = request.POST.get("name")
        color = request.POST.get("color")
        manufact = request.POST.get("manufact")
        price = request.POST.get("price")
        item = Rim(name_rim=name, id_color_id=color, manufact=manufact, price=price)
        item.save()
    return render(request, 'main/add_rim.html')


def add_lenses(request):
    if request.method == "POST":
        name = request.POST.get("name")
        color = request.POST.get("color")
        manufact = request.POST.get("manufact")
        price = request.POST.get("price")
        #item = NotImplementedError(name_rim=name, id_color_id=color, manufact=manufact, price=price)
        #item.save()
    return render(request, 'main/add_lenses.html')


def add_accessories(request):
    if request.method == "POST":
        name = request.POST.get("name")
        type = request.POST.get("type")
        manufact = request.POST.get("manufact")
        price = request.POST.get("price")
        with connection.cursor() as cursor:
            cursor.execute("UPDATE accessories SET manu ='Tomas' WHERE Univ_Id=1 ")
    return render(request, 'main/add_accessories.html')


def overdue_order(request):
    order = OverdueOrder.objects.all()
    return render(request, 'main/overdue_order.html',{'order': order})


def customer(request):
    customer1 = Customer.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        email = request.POST.get("email")
        with connection.cursor() as cursor:
            cursor.execute("exec [create_customer] %s, %s, %s, %s",
                           [name, surname, phone_number, email])
    return render(request, 'main/customer.html',{'customers': customer1})


def shop_employee(request):
    shop_employee1 = ShopEmployee.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        patronymic = request.POST.get("patronymic")
        post = request.POST.get("post")
        phone_number = request.POST.get("phone_number")
        passport_details = request.POST.get("passport_details")
        adress = request.POST.get("adress")
        item = ShopEmployee(name=name, surname=surname, patronymic=patronymic, post=post,
                            phone_number=phone_number, passport_details=passport_details, adress=adress)
        item.save()
    return render(request, 'main/shop_employee.html', { 'shop_employee': shop_employee1 })


def eye_doctor(request):
    eye_doctor1 = EyeDoctor.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        patronymic = request.POST.get("patronymic")
        post = request.POST.get("post")
        phone_number = request.POST.get("phone_number")
        passport_details = request.POST.get("passport_details")
        adress = request.POST.get("adress")
        item = EyeDoctor(name=name, surname=surname, patronymic=patronymic, post=post,
                         phone_number=phone_number, passport_details=passport_details, adress=adress)
        item.save()
    return render(request, 'main/eye_doctor.html',{'eye_doctor': eye_doctor1})


def order(request):
    order1 = Orderr.objects.all()
    if request.method == "POST":
        id_employee = request.POST.get("id_employee")
        id_prescription = request.POST.get("id_prescription")
        date_acceptance = request.POST.get("date_acceptance")
        date_assignment = request.POST.get("date_assignment")
        id_status = request.POST.get("id_status")
        end_price = request.POST.get("end_price")
        with connection.cursor() as cursor:
            cursor.execute("exec [create_order] %s, %s, %s, %s, %s, %s",
                           [id_employee, id_prescription, date_acceptance, date_assignment, id_status, end_price])
    return render(request, 'main/order.html',{'order': order1})


def add_item_order(request):
    if request.method == "POST":
        id_catalog = request.POST.get("id_catalog")
        id_order = request.POST.get("id_order")
        quantity = request.POST.get("quantity")
        item = OrderList(id_catalog_id=id_catalog, id_order_id=id_order, quantity=quantity)
        item.save()
    return render(request, 'main/add_item_order.html')


def prescription(request):
    prescription1 = Prescription.objects.all()
    if request.method == "POST":
        id_employee = request.POST.get("id_employee")
        id_customer = request.POST.get("id_customer")
        right_diopter = request.POST.get("right_diopter")
        left_diopter = request.POST.get("left_diopter")
        distance = request.POST.get("distance")
        date = request.POST.get("date")
        with connection.cursor() as cursor:
            cursor.execute("exec [create_prescription] %s, %s, %s, %s, %s, %s",
                           [id_employee,id_customer,right_diopter,left_diopter,distance,date])
    return render(request, 'main/prescription.html',{'prescription': prescription1})


def delete_prescription(request, my_id):
    item = Prescription.object.get(id_prescribtion=my_id)
    if request.method == "POST":
        item.delete()
        return redirect
    return render(request, 'main/delete_prescription.html', {"item": item})


def update_catalog(request):
    if request.method == "POST":
        name = request.POST.get("name")
        type = request.POST.get("type")
        manufact = request.POST.get("manufact")
        price = request.POST.get("price")
        item = Rim(name_rim=name, type=type, manufact=manufact, price=price)
        item.save()
    return render(request, 'main/update_catalog.html')

