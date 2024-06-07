from django.shortcuts import render,redirect
from .forms import productAddform, MyproteinAddform 
from django.contrib import messages
from .models import productdetails, usercoment
from .models import Myproteindetails
from django.contrib.auth.decorators import login_required


@login_required(login_url='singIn')
def Myproducts(request):
    form = productAddform()
    product =productdetails.objects.all()
    print(product)
    if request.method == "POST":
        form = productAddform(request.POST,request.FILES)
        if form.is_valid():
            product =form.save()
            product.merchant =request.user
            product.save()
            messages.success(request,"product Data saved")
            return redirect("Myproducts")
        else:
            messages.info(request,"Product Not Saved")
            return redirect("Myproducts")

    context ={
        "form":form,
        "product":product
    }
    return render(request,'product.html',context)


@login_required(login_url='singIn')
def Myprotein(request):
    form = MyproteinAddform()
    product =Myproteindetails.objects.all()
    print(product)
    if request.method == "POST":
        form = MyproteinAddform(request.POST,request.FILES)
        if form.is_valid():
            product =form.save()
            product.merchant =request.user
            product.save()
            messages.success(request,"product Data saved")
            return redirect("Myprotein")
        else:
            messages.info(request,"Product Not Saved")
            return redirect("Myprotein")

    context ={
        "form":form,
        "product":product
    }
    return render(request,'protein.html',context)



def proteinsingleview(request,pk):
    protein=Myproteindetails.objects.get(id=pk)
    comm = usercoment.objects.filter(protein = protein )


    context ={ 
        "protein":protein,
        "comm":comm
    }
    return render(request,'proteinsingleview.html',context)




# @login_required(login_url='SignIn')
# def productsingleview(request,pk):
#     product =productdetails.objects.get(id=pk)

#     context ={
#         "product":product
#     }
#     return render(request,"workout.html",context)