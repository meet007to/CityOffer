from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from app1.models import ShopKeeper, Customer
from .models import Category, SubCategory, Admin
from .forms import CatForm, SubForm, AdminForm
from app1.forms import ShopKeeperForm, CustomerForm
from django.contrib import messages


# Create your views here.
def AdminLogin(request):
    if request.session.keys():
        return redirect("/admin1/shopkeeperlist/")
    else:
        if request.method == "POST":
            try:
                obj = Admin.objects.get(email=request.POST["email"])
                if obj.password == request.POST["password"]:
                    request.session['name'] = obj.name
                    return redirect("/admin1/shopkeeperlist/")
                else:
                    messages.info(request, "Wrong Password")
                    return redirect("/admin1/")
            except:
                messages.info(request, "Wrong Username")
                return redirect("/admin1/")

        return render(request, "login1.html")


def LogOut(request):
    if request.session.keys():
        request.session.flush()
        return HttpResponseRedirect("/admin1/")
    else:
        return render(request, "login1.html")


def CategoryList(request):
    if request.session.keys():
        data = Category.objects.all
        return render(request, "catlist.html", {"data": data})
    else:
        return redirect("/admin1/")


def SubCategoryList(request):
    if request.session.keys():
        data = SubCategory.objects.all
        return render(request, "sublist.html", {"data1": data})
    else:
        return redirect("/admin1/")


def AddSub(request):
    key6 = Category.objects.all
    form = SubForm(request.POST)
    if form.is_valid():
        if SubCategory.objects.filter(catname=request.POST["catname"], subname=request.POST["subname"]):
            messages.info(
                request, "CategoryName And Subcategory are Already Availbale")
            return redirect("/admin1/addsub/")
        form.save()
        return redirect('/admin1/subcategorylist/')
    return render(request, "add-sub.html", {"key5": form, "key6": key6})


def AddCat(request):
    form = CatForm(request.POST)
    if form.is_valid():
        if Category.objects.filter(catname=request.POST["catname"]):
            messages.warning(request, "CategoryName IS Already Availbale")
            return redirect('/admin1/add-cat/')

        form.save()
        return redirect("/admin1/categorylist/")
    return render(request, "add-cat.html", {"key4": form})


def EditCat(request, id):
    data = Category.objects.get(id=id)
    form = CatForm(request.POST, instance=data)
    if form.is_valid():
        form.save()
        return redirect("/admin1/categorylist/")
    return render(request, "editcat.html", {"key3": data})


def EditSub(request, id):
    data = SubCategory.objects.get(id=id)
    data1 = Category.objects.all
    form = SubForm(request.POST, instance=data)
    if form.is_valid():
        form.save()
        return redirect("/admin1/subcategorylist/")
    return render(request, "editsub.html", {"key3": data, "data1": data1})


def DeleteSub(request, id):
    data = SubCategory.objects.get(id=id)
    data.delete()
    return redirect("/admin1/subcategorylist/")


def DeleteCat(request, id):
    data = Category.objects.get(id=id)
    data.delete()
    return redirect("/admin1/categorylist/")


def FeedBack(request):
    return HttpResponse("WelCome User")


def CustomerList(request):
    if request.session.keys():
        data = Customer.objects.all()
        return render(request, "clist.html", {"customer": data})
    else:
        return redirect("/admin1/")


def EditCustomer(request, email):
    data = Customer.objects.get(cemail=email)
    return render(request, "editcustomer.html", {"key2": data})


def UpdateCustomer(request, email):
    data = Customer.objects.get(cemail=email)
    form = CustomerForm(request.POST, instance="data")
    if form.is_valid:
        obj = Customer.objects.get(cemail=email)

        obj.firstname = request.POST["firstname"]
        obj.lastname = request.POST["lastname"]
        obj.dob = request.POST["dob"]
        obj.gender = request.POST["gender"]
        obj.address = request.POST["address"]
        obj.mobile = request.POST["mobile"]
        if obj.cemail != request.POST["cemail"]:
            obj.cemail = request.POST["cemail"]
            if Customer.objects.filter(cemail=request.POST["cemail"]):
                messages.warning(request, "Email Is all ready Exists")
                return HttpResponse("Not Updated")
        obj.password = request.POST["password"]
        obj.pincode = request.POST["pincode"]
        obj.state = request.POST["state"]
        obj.city = request.POST["city"]
        # obj.simage = request.POST["simage"]

        obj.save()
        return redirect("/admin1/customerlist/")
    return render(request, "editcustomer.html", {"key2": data})


def DeleteCustomer(request, email):

    obj = Customer.objects.get(cemail=email)
    obj.delete()
    return redirect("/admin1/customerlist/")


def ShopkeeperList(request):
    if request.session.keys():
        data = ShopKeeper.objects.all()
        return render(request, "slist.html", {"shopkeeper": data})

    else:
        return redirect("/admin1/")


def EditShopkeeper(request, email):
    data = ShopKeeper.objects.get(semail=email)
    return render(request, "editshopkeeper.html", {"key1": data})


def UpdateShopKeeper(request, email):
    data = ShopKeeper.objects.get(semail=email)
    form = ShopKeeperForm(request.POST, instance="data")
    if form.is_valid:
        obj = ShopKeeper.objects.get(semail=email)
        testemail = obj.semail
        if obj.shopname != request.POST["shopname"]:
            obj.shopname = request.POST["shopname"]
        else:
            obj.shopname = obj.shopname
        obj.firstname = request.POST["firstname"]
        obj.lastname = request.POST["lastname"]
        # obj.dob = request.POST['dob']
        obj.gender = request.POST["gender"]
        obj.address = request.POST["address"]
        obj.mobile = request.POST["mobile"]
        obj.semail = request.POST["semail"]
        obj.password = request.POST["password"]
        obj.pincode = request.POST["pincode"]
        obj.state = request.POST["state"]
        obj.city = request.POST["city"]
        # obj.simage = request.POST["simage"]
        if obj.semail != testemail:
            if ShopKeeper.objects.filter(semail=request.POST["semail"]):
                messages.warning(request, "Email Is all ready Exists")

        obj.save()
        return HttpResponseRedirect("/admin1/shopkeeperlist/")

    return render(request, "editshopkeepr.html", {"key1": data})


def DeleteShopKeeper(request, email):

    obj = ShopKeeper.objects.get(semail=email)
    obj.delete()
    return redirect("/admin1/shopkeeperlist/")


def Profile(request):
    if request.session.keys():

        data = Admin.objects.get(id=1)
        return render(request, "profile.html", {"key6": data})
    else:
        return redirect("/admin1/")


def EditProfile(request, id):
    data = Admin.objects.get(id=id)
    form = AdminForm(request.POST, instance=data)
    if form.is_valid():
        form.save()
        return redirect("/admin1/profile/")
    # obj.name = request.POST["name"]
    # obj.email = request.POST["email"]
    # obj.password = request.POST["password"]

    return render(request, "editprofile.html", {"key7": data})
