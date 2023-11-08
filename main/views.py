from django.shortcuts import render, redirect
from django.db import connection
from .models import Accessories, Catalog, Color, Customer, EyeDoctor, Lenses, OrderList, Orderr, Prescription, Rim,\
    ShopEmployee, Status, OverdueOrder, OrderListByIdOrder, OrderrWithoutId,PrescriptionWithoutId, \
    AccessoriesWithQuantity, LensesWithQuantity, RimWithQuantity
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    rim = Rim.objects.all()
    lenses = Lenses.objects.all()
    accessories = Accessories.objects.all()
    return render(request, 'main/home.html', {'title': 'Главная страница сайта', 'rim': rim, 'lenses': lenses, 'accessories': accessories})

@login_required()

def about_us(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM hello_person WHERE name = 'Tomas'")
        row = cursor.fetchone()  # получаем одну строку
    return render(request, 'main/overdue_order.html')

@login_required()

def add_item(request):
    rim = Rim.objects.all()
    lenses = Lenses.objects.all()
    accessories = Accessories.objects.all()
    return render(request, 'main/add_item.html',{'title': 'Товары','rim': rim, 'lenses': lenses, 'accessories': accessories})

@login_required()

def add_rim(request):
    rim = RimWithQuantity.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        #color = request.POST.get("color")
        color_name = request.POST.get("color_name")
        with connection.cursor() as cursor:
            cursor.execute("SELECT dbo.id_color(%s)", [color_name])
            color_id = cursor.fetchone()[0]
        manufact = request.POST.get("manufact")
        price = request.POST.get("price")
        item = Rim(name_rim=name, id_color_id=color_id, manufact=manufact, price=price)
        item.save()
    return render(request, 'main/add_rim.html', {"item": rim})

@login_required()

def add_lenses(request):
    lenses = LensesWithQuantity.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        # color = request.POST.get("color")
        color_name = request.POST.get("color_name")
        with connection.cursor() as cursor:
            cursor.execute("SELECT dbo.id_color(%s)", [color_name])
            color_id = cursor.fetchone()[0]
            manufact = request.POST.get("manufact")
        price = request.POST.get("price")
        diopter = request.POST.get("diopter")
        item = Lenses(name_lenses=name, id_color_id=color_id, manufact=manufact, price=price, diopter=diopter)
        item.save()
    return render(request, 'main/add_lenses.html', {"item": lenses})

@login_required()

def add_accessories(request):
    accessories = AccessoriesWithQuantity.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        type = request.POST.get("type")
        manufact = request.POST.get("manufact")
        price = request.POST.get("price")
        item = Accessories(name_accessories=name, type=type, manufact=manufact, price=price)
        item.save()
    return render(request, 'main/add_accessories.html', {"item": accessories})

@login_required()

def update_quantity_rim(request, my_id):
    item = Catalog.objects.get(id_rim=my_id)
    if request.method == "POST":
        quantity1 = item.quantity
        quantity2 = int(request.POST.get("quantity"))
        item.quantity = quantity1 + quantity2
        item.save()
        return redirect("add_rim")
    return render(request, 'main/update_quantity.html')

@login_required()

def update_quantity_lenses(request, my_id):
    item = Catalog.objects.get(id_lenses=my_id)
    if request.method == "POST":
        quantity1 = item.quantity
        quantity2 = int(request.POST.get("quantity"))
        item.quantity = quantity1 + quantity2
        item.save()
        return redirect("add_lenses")
    return render(request, 'main/update_quantity.html')

@login_required()

def update_quantity_accessories(request, my_id):
    item = Catalog.objects.get(id_accessories=my_id)
    if request.method == "POST":
        quantity1 = item.quantity
        quantity2 = int(request.POST.get("quantity"))
        item.quantity = quantity1 + quantity2
        item.save()
        return redirect("add_accessories")
    return render(request, 'main/update_quantity.html')

@login_required()

def overdue_order(request):
    order = OverdueOrder.objects.all()
    return render(request, 'main/overdue_order.html',{'order': order})

@login_required()

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

@login_required()

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

@login_required()

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

@login_required()

def order(request):
    order1 = OrderrWithoutId.objects.filter(id_status_id=1)
    order2 = OrderrWithoutId.objects.filter(id_status_id=2)
    order3 = OrderrWithoutId.objects.filter(id_status_id=3)
    order4 = OrderrWithoutId.objects.filter(id_status_id=4)

    if request.method == "POST":
        #id_employee = request.POST.get("id_employee")
        employee_name = request.POST.get("employee_name")
        employee_surname = request.POST.get("employee_surname")
        with connection.cursor() as cursor:
            cursor.execute("SELECT dbo.shop_employee_id(%s,%s)", [employee_name, employee_surname])
            id_employee = cursor.fetchone()[0]
        #id_prescription = request.POST.get("id_prescription")
        customer_name = request.POST.get("customer_name")
        customer_surname = request.POST.get("customer_surname")
        with connection.cursor() as cursor:
            cursor.execute("SELECT dbo.customer_prescription(%s,%s)", [customer_name, customer_surname])
            id_prescription = cursor.fetchone()[0]
        date_acceptance = request.POST.get("date_acceptance")
        with connection.cursor() as cursor:
            cursor.execute("exec [create_order] %s, %s, %s",
                           [id_employee, id_prescription, date_acceptance])
    return render(request, 'main/order.html',{'order1': order1,'order2': order2,'order3': order3,'order4': order4,})

@login_required()

def create_order(request, my_id):
    order1 = OrderrWithoutId.objects.filter(id_status_id=1)
    order2 = OrderrWithoutId.objects.filter(id_status_id=2)
    order3 = OrderrWithoutId.objects.filter(id_status_id=3)
    order4 = OrderrWithoutId.objects.filter(id_status_id=4)

    if request.method == "POST":
        id_employee = request.POST.get("id_employee")
        # id_prescription = request.POST.get("id_prescription")
        id_customer = request.POST.get("id_customer")
        with connection.cursor() as cursor:
            cursor.execute("SELECT dbo.customer_prescription(%s)", [id_customer])
            id_prescription = cursor.fetchone()[0]
        date_acceptance = request.POST.get("date_acceptance")
        with connection.cursor() as cursor:
            cursor.execute("exec [create_order] %s, %s, %s",
                           [id_employee, id_prescription, date_acceptance])
    return render(request, 'main/create_order.html',
                  {'order1': order1, 'order2': order2, 'order3': order3, 'order4': order4, 'my_id': my_id })

@login_required()

def delete_order(request, my_id):
    item = Orderr.objects.get(id_order=my_id)
    if request.method == "POST":
        item.delete()
        return redirect("order")
    return render(request, 'main/delete_confirm.html', {"item": item})

@login_required()

def update_status1(request, my_id):
    item = Orderr.objects.get(id_order=my_id)
    if request.method == "POST":
        item.id_status_id = 2
        item.save()
        return redirect("order")
    return render(request, 'main/update_status1.html', {"item": item})

@login_required()

def update_status2(request, my_id):
    item = Orderr.objects.get(id_order=my_id)
    if request.method == "POST":
        item.id_status_id = 3
        item.save()
        return redirect("order")
    return render(request, 'main/update_status2.html', {"item": item})

@login_required()

def update_status3(request, my_id):
    item = Orderr.objects.get(id_order=my_id)
    if request.method == "POST":
        item.id_status_id = 4
        #item.save()
        with connection.cursor() as cursor:
            cursor.execute("exec [change_status] %s, %s",
                           [item.id_status_id, my_id])
        return redirect("order")
    return render(request, 'main/update_status3.html', {"item": item})




@login_required()

def order_list_by_id_order(request, my_id):
    item = OrderListByIdOrder.objects.raw("select * from dbo.[order_list_orderr_id](%s)", [my_id])
    if request.method == "POST":
        #id_catalog = request.POST.get("id_catalog")
        name_item = request.POST.get("name_item")
        manufact_item = request.POST.get("manufact_item")
        with connection.cursor() as cursor:
            cursor.execute("SELECT dbo.catalog_id(%s,%s)", [name_item, manufact_item])
            id_catalog = cursor.fetchone()[0]
        id_order = my_id
        quantity = request.POST.get("quantity")
        item2 = OrderList(id_catalog_id=id_catalog, id_order_id=id_order, quantity=quantity)
        item2.save()
    return render(request, 'main/order_list_by_id_order.html', {"item": item})

@login_required()

def prescription(request):
    prescription1 = PrescriptionWithoutId.objects.all()
    if request.method == "POST":
        #id_employee = request.POST.get("id_employee")
        employee_name = request.POST.get("employee_name")
        employee_surname = request.POST.get("employee_surname")
        with connection.cursor() as cursor:
            cursor.execute("SELECT dbo.eye_doctor_id(%s, %s)", [employee_name, employee_surname])
            id_employee = cursor.fetchone()[0]

        #id_customer = request.POST.get("id_customer")
        name = request.POST.get("customer_name")
        surname = request.POST.get("customer_surname")
        with connection.cursor() as cursor:
            cursor.execute("SELECT dbo.customer_id(%s,%s)", [name , surname])
            id_customer = cursor.fetchone()[0]
        right_diopter = request.POST.get("right_diopter")
        left_diopter = request.POST.get("left_diopter")
        distance = request.POST.get("distance")
        date = request.POST.get("date")
        with connection.cursor() as cursor:
            cursor.execute("exec [create_prescription] %s, %s, %s, %s, %s, %s",
                           [id_employee,id_customer,right_diopter,left_diopter,distance,date])
    return render(request, 'main/prescription.html',{'prescription': prescription1})

@login_required()

def create_prescription(request, my_id):
    prescription1 = PrescriptionWithoutId.objects.all()
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
    return render(request, 'main/create_prescription.html',{'prescription': prescription1, 'my_id': my_id})

@login_required()

def delete_prescription(request, my_id):
    item = Prescription.objects.get(id_prescribtion=my_id)
    if request.method == "POST":
        item.delete()
        return redirect("prescription")
    return render(request, 'main/delete_confirm.html', {"item": item})

@login_required()

def last_prescription(request, my_id):
    #item = PrescriptionWithoutId.objects.filter(id_customer=my_id)
    item = PrescriptionWithoutId.objects.raw("select * from dbo.[customer_last_prescription](%s)", [my_id])
    return render(request, 'main/last_prescription.html', {"item": item})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
        #return redirect("/users/register")
    form = NewUserForm()
    context = {
        'form': form
    }
    return render(request, 'main/register.html', context)

@login_required()
def profile(request):
    return render(request, "main/profile.html")

@login_required()
def profileemployee(request):
    return render(request, "main/profile.html")

@login_required()
def profiledoctor(request):
    return render(request, "main/profile.html")


