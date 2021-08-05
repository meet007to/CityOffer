from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer, ShopKeeper, Order
from .forms import ShopKeeperForm, CustomerForm
from adminsite.models import SubCategory, Category
from shopkeeper.models import Product
from shopkeeper.forms import CartAddProductForm
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.


def Index(request):
    obj1 = Category.objects.all()
    obj2 = SubCategory.objects.all()
    obj3 = Product.objects.all()
    no = 7
    # list(obj3)[:7]
    return render(request, "index.html", {"cat": obj1, "sub": obj2, "product": list(obj3), "no": no})


def LoginCustomer(request):
    if request.session.keys():
        return redirect("/")
    else:
        if request.method == "POST":
            try:
                obj = Customer.objects.get(cemail=request.POST["cemail"])
                if obj.password == request.POST["password"]:
                    request.session['customeremail'] = obj.cemail
                    return redirect("/")

                else:
                    messages.info(request, "Wrong Password")
                    return redirect("/login.html/")
            except:
                messages.info(request, "Wrong Username")
                return redirect("/login.html/")
        return render(request, "login.html")


def LoginShopkeeper(request):
    if request.session.keys():
        return redirect("/shopkeeper/ab/")
    else:
        if request.method == "POST":
            try:
                obj = ShopKeeper.objects.get(semail=request.POST["semail"])
                if obj.password == request.POST["password"]:
                    request.session['email'] = obj.semail
                    return redirect("/shopkeeper/ab/")

                else:
                    messages.info(request, "Wrong Password")
                    return redirect("/shopkeeperlogin.html/")
            except:
                messages.info(request, "Wrong Username")
                return redirect("/shopkeeperlogin.html/")
        return render(request, "shopkeeperlogin.html")


def CustomerRegistration(request):
    form = CustomerForm(request.POST)
    if form.is_valid():
        obj = Customer()
        obj.firstname = request.POST["firstname"]
        obj.lastname = request.POST["lastname"]
        obj.dob = request.POST["dob"]
        obj.gender = request.POST["gender"]
        obj.address = request.POST["address"]
        obj.mobile = request.POST["mobile"]
        obj.cemail = request.POST["cemail"]
        obj.password = request.POST["password"]
        obj.pincode = request.POST["pincode"]
        obj.state = request.POST["state"]
        obj.city = request.POST["city"]

        if Customer.objects.filter(cemail=request.POST["cemail"]).exists():
            messages.warning(request, "Email Is all ready Exists")

            return redirect("/cregistration.html/",)

        if request.POST["password"] != request.POST["password1"]:
            messages.info(request, 'Password Not Match')

            return redirect("/cregistration.html/")

        obj.save()
        return redirect("/login.html/")
    return render(request, "cregistration.html")


def ShopkeeperRegistration(request):
    form = ShopKeeperForm(request.POST)
    if form.is_valid():
        obj = ShopKeeper()
        obj.shopname = request.POST["shopname"]
        obj.firstname = request.POST["firstname"]
        obj.lastname = request.POST["lastname"]
        obj.dob = request.POST["dob"]
        obj.gender = request.POST["gender"]
        obj.address = request.POST["address"]
        obj.mobile = request.POST["mobile"]
        obj.semail = request.POST["semail"]
        obj.password = request.POST["password"]
        obj.pincode = request.POST["pincode"]
        obj.state = request.POST["state"]
        obj.city = request.POST["city"]

        if ShopKeeper.objects.filter(semail=request.POST["semail"]):
            messages.warning(request, "Email Is all ready Exists")

            return redirect("/sregistration.html/",)

        if ShopKeeper.objects.filter(shopname=request.POST["shopname"]):
            messages.info(request, "Shopname is Already Choosen")
            return redirect("//",)

        if request.POST["password"] != request.POST["password1"]:
            messages.info(request, 'Password Not Match')

            return redirect("/sregistration.html/")

        obj.save()
        return redirect("/login.html/")

    return render(request, "sregistration.html")


def Clogout(request):
    if request.session.keys():
        request.session.flush()
        return HttpResponseRedirect("/")
    else:
        return render(request, "/")


def ProductView(request, id):
    if request.session.keys():
        obj1 = Category.objects.all()
        obj2 = SubCategory.objects.all()
        # obj = Product.objects.get(id=id)

        book = Product.objects.get(id=id)
        cart_product_form = CartAddProductForm()
        context = {
            'data': book,
            'cat': obj1,
            'sub': obj2,
            'cart_product_form': cart_product_form
        }
        return render(request, 'productview.html', context)
    else:
        return redirect('/')


def Cart(request, id):
    cart = Order()
    user = Customer.objects.get(cemail=request.session['customeremail'])
    product = get_object_or_404(Product, id=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.semail = product.email
        cart.cemail = user
        cart.name = product.name
        cart.quantity = request.POST['quantity']
        cart.price = int(product.price) * int(cart.quantity)
        cart.save()
        return redirect('corders')


def orders(request):
    if request.session.keys():
        tot = 0
        cemail1 = Customer.objects.get(cemail=request.session['customeremail'])

        show_data = Order.objects.filter(
            cemail=cemail1).filter(status="pending")
        for i in show_data:
            tot += i.price
        # request.session['Order_total'] = tot

        return render(request, 'cart.html', {'data': show_data, 'total': tot, 'User': cemail1})
    else:
        return redirect('/')


def chackout(request):
    # return render(request, "chackout.html")
    cemail2 = Customer.objects.get(cemail=request.session['customeremail'])
    data = Order.objects.filter(
        cemail=cemail2).filter(status="pending").update(status="success")
    show_data = Order.objects.filter(
        cemail=cemail2).filter(status="success")

    return render(request, 'chackout.html', {'data': show_data, 'User': cemail2})


def cart_remove(request, id):
    product = Order.objects.get(id=id)
    product.delete()
    return redirect('corder')


def filterproduct(request, id, str):
    obj1 = Category.objects.all()
    obj2 = SubCategory.objects.all()

    obj3 = Product.objects.filter(
        catname_id=id).filter(subname=str)

    return render(request, "index.html", {"cat": obj1, "sub": obj2, "product": obj3})


def Cprofile(request):
    data = Customer.objects.get(cemail=request.session["customeremail"])
    return render(request, "cprofile.html", {"data": data})
