from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from app1.models import ShopKeeper, Customer
from app1.forms import ShopKeeperForm
from adminsite.models import SubCategory, Category
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product
from app1.models import Order


class PersonListView(ListView):

    model = Product
    context_object_name = 'people'

    def get_queryset(self, *args, **kwargs):
        qs = super(PersonListView, self).get_queryset(
            *args, **kwargs).filter(email=self.request.session["email"])
        # print(qs)
        return qs


class PersonCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('person_changelist')

    def get_initial(self):
        initial = super(PersonCreateView, self).get_initial()
        initial = {'email': self.request.session['email']}
        return initial


class PersonUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('person_changelist')


def load_cities(request):
    catname_id = request.GET.get('catname')
    subcat = SubCategory.objects.filter(
        catname_id=catname_id).order_by('subname')
    print(subcat)
    return render(request, 'shopkeeper/sub_list_options.html', {'subcat': subcat})


# def Product(request):
#     data = ShopKeeper.objects.get(semail=request.session['email'])
#     return render(request, "shopkeeper/product_list.html", {"obj": data})


def Order1(request):
    if request.session.keys():

        semail1 = ShopKeeper.objects.get(semail=request.session['email'])

        show_data = Order.objects.filter(
            semail=semail1)

        return render(request, 'sorder.html', {'data': show_data})
    else:
        return redirect('/')


def Profile(request):
    data1 = ShopKeeper.objects.get(semail=request.session['email'])
    form = ShopKeeper(request.POST)
    return render(request, "sprofile.html", {"obj1": data1, "form": form},)


def EditsProfile(request):
    data2 = ShopKeeper.objects.get(semail=request.session['email'])
    form = ShopKeeperForm(request.POST, request.FILES, instance=data2)
    if request.method == "POST":
        obj = ShopKeeper.objects.get(semail=request.session['email'])
        print(obj)
        if obj.shopname != request.POST["shopname"]:
            if ShopKeeper.objects.filter(shopname=request.POST["shopname"]):
                messages.warning(request, "Shopname Is all ready Exists")
                return redirect("/shopkeeper/editsprofile/", {"obj2": data2, "form": form})

            obj.shopname = request.POST["shopname"]
        else:
            obj.shopname == obj.shopname
        obj.firstname = request.POST["firstname"]
        obj.lastname = request.POST["lastname"]
        obj.dob = request.POST["dob"]
        # obj.gender = request.POST["gender"]
        obj.address = request.POST["address"]
        obj.mobile = request.POST["mobile"]
        obj.password = request.POST["password"]
        obj.pincode = request.POST["pincode"]
        obj.state = request.POST["state"]
        obj.city = request.POST["city"]
        obj.save()
        return redirect("/shopkeeper/sprofile/")
    else:
        return render(request, "editsprofile.html", {"obj2": data2, "form": form})


def Slogout(request):
    if request.session.keys():
        request.session.flush()
        return HttpResponseRedirect("/shopkeeperlogin.html/")
    else:
        return render(request, "login1.html")
