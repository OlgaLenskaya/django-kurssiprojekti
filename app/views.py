from django.shortcuts import render, redirect
from .models import Supplier, Product
from django.contrib.auth import authenticate, login, logout

def landingview(request):
    return render (request, 'landingpage.html')

# AFTER LOGIN

def loginview(request):
    return render (request, "login.html")

# LOGIN AND LOGOUT

def loginview(request):
    return render (request, "login.html")

def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    user = authenticate(username = user, password = passw)
    if user:
        login(request, user)
        context = {'name': user}
        return render(request,'landingpage.html',context)
    else:
        return render(request, 'loginerror.html')

def logout_action(request):
    logout(request)
    return render(request, 'login.html')


# SUPPLIERS

def supplierlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplierlist = Supplier.objects.all()
        context = {'suppliers': supplierlist}
        return render (request,"suppliers.html",context)

def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def deletesupplier(request, id):
    Supplier.objects.filter(id = id).delete()
    return redirect(request.META['HTTP_REFERER'])

def edit_supplier_get(request, id):
    supplier = Supplier.objects.filter(id = id)
    context = {'supplier': supplier}
    return render (request,"edit_supplier.html",context)

def edit_supplier_post(request, id):
    item = Supplier.objects.get(id = id)
    item.contactname = request.POST['contactname']
    item.address = request.POST['address']
    item.phone = request.POST['phone']
    item.email = request.POST['email']
    item.country = request.POST['country']
    item.save()
    return redirect(supplierlistview)

def searchsuppliers(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        search = request.POST['search']
        filtered = Supplier.objects.filter(companyname__icontains=search)
        context = {'suppliers': filtered}
        return render (request,"suppliers.html",context)

# PRODUCTS

def productlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        context = {'products': productlist}
        return render (request,"products.html",context)

def addproduct(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['productname']
        b = request.POST['packagesize']
        c = request.POST['unitprice']
        d = request.POST['unitsinstock']
        e = request.POST['companyname']
        Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, companyname = e).save()
        return redirect(request.META['HTTP_REFERER'])


def deleteproduct(request, id):
    
    Product.objects.filter(id = id).delete()
    return redirect(request.META['HTTP_REFERER'])

def edit_product_get(request, id):
    
    product = Product.objects.filter(id = id)
    context = {'product': product}
    return render (request,"edit_product.html",context)

def edit_product_post(request, id):
   
    item = Product.objects.get(id = id)
    item.unitprice = request.POST['unitprice']
    item.unitsinstock = request.POST['unitsinstock']
    item.packagesize = request.POST['packagesize']
    item.save()
    return redirect(productlistview)

def products_filtered(request, id):
    
    productlist = Product.objects.all()
    filteredproducts = productlist.filter(supplier = id)
    context = {'products': filteredproducts}
    return render (request,"products.html",context)