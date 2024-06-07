from django.shortcuts import render,HttpResponse,redirect
from .forms import userADDfrom
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorator import AdminDecorator
from product.models import Myproteindetails,cart, Comment,usercoment
from product.forms import MyproteinAddform
from django.contrib.auth.decorators import login_required
from product.models import productdetails




@AdminDecorator
def Index(request):
    return render(request,'merchant.html')

def proteinpowder(request):
    form = MyproteinAddform()
    Myprotein = Myproteindetails.objects.filter(merchant = request.user)
    print = (Myprotein)
    if request.method == "POST":
        form = MyproteinAddform(request.POST,request.FILES)
        if form.is_valid():
            product =form.save()
            product.merchant =request.user
            product.save()
            messages.success(request,"product Data saved")
            return redirect("proteinpowder")
        else:
            messages.info(request,"Product Not Saved")
            return redirect("proteinpowder")
    context = {
        "form":form,
        "Myprotein":Myprotein
    }
    return render(request,'proteinpowder.html',context)

def merchant(request):
    return render(request,'merchant.html')

def Home(request):
    return render(request,'Index.html')

def proteinsingleview(request,pk):
    protein = Myproteindetails.objects.get(id =pk)

    context ={
        "protein":protein
    }

    return render(request,'proteinsingleview.html',context)

@login_required(login_url='singIn')
def userIndex(request):
    return render (request,"userIndex.html")

def workout(request):
    workout = productdetails.objects.all()

    context = {
        "workout":workout
    }
    return render(request,"workout.html",context)

def about(request):
    return render(request,"about.html")             

def team(request):
    return render(request,"team.html")

def contact(request):
    return render(request,"contact.html")
    
def detail(request):
    return render(request,"detail.html")

def blog(request):
    return render(request,"blog.html")


@login_required(login_url='singIn')
def carts(request):
    carts = cart.objects.all()

    context = {
        "carts":carts
    }
    return render(request,"cart.html",context)




def commentsection(request,pk):

    workout = productdetails.objects.get(id =pk)
    comm = Comment.objects.filter(video = workout )

    context ={
        "workout":workout,
        "comm":comm
    }

    return render(request,"commentsection.html",context)

def Comments(request,pk):
    product = productdetails.objects.get(id = pk)
    if request.method == "POST":
        comment = request.POST['comment']
        val = Comment.objects.create(video = product,user=request.user, body = comment )
        val.save()
        return redirect(commentsection, pk= pk)

    return redirect('commentsection', pk = pk)


def customercomentsection(request,pk):

    Myprotein = Myproteindetails.objects.get(id =pk)
    comm = usercoment.objects.filter(protein = Myprotein )

    context ={
        "Myprotein":Myprotein,
        "comm":comm
    }

    return render(request,"proteinsingleview.html",context)


def customercoment(request,pk):
    product = Myproteindetails.objects.get(id = pk)
    if request.method == "POST":
        comment = request.POST['comment']
        val = usercoment.objects.create(protein = product,user=request.user, body = comment )
        val.save()
        return redirect(proteinsingleview,pk= pk)

    return redirect('proteinsingleview',pk = pk)


def testimonial(request):
    return render(request,"testimonial.html")

def protein(request):
    protein =Myproteindetails.objects.all()
   

    context = {
        "protein":protein
    }

    return render(request,"protein.html",context)


def deletecart(request,pk):

    cart.objects.get(id=pk).delete()
    messages.info(request,"cart data deleted...")
    return redirect("carts")

def deleteworkout(request,pk):

    productdetails.objects.get(id=pk).delete()
    messages.info(request,"workout data deleted...")
    return redirect("Myproducts")

def deleteprotein(request,pk):

    Myproteindetails.objects.get(id=pk).delete()
    messages.info(request,"protein data deleted...")
    return redirect("proteinpowder")


def signUp(request):
    form = userADDfrom()
    if request.method == "POST":
        form = userADDfrom(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request,"user created")
            return redirect("singIn")
        
    context ={
    "form":form
    }
    return render(request,'Register.html',context)

def singIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Index")  # Corrected redirection
        else:
            messages.info(request, "Username or password incorrect")
            return redirect("singIn")
    return render(request, 'Login.html')

def signout(request):
    logout(request)
    return redirect('singIn')


def AddToCart(request,pk):
    pro = Myproteindetails.objects.get(id =pk)
    carts = cart.objects.create(products =pro,quantity =1,user =request.user,totalprice =pro.product_price)
    
    carts.save()
    messages.info(request,"Product Added To The cart seaction")
    return redirect('carts')


def IncreaseCartQuantity(request,pk):
    cartitem = cart.objects.get(id = pk)
    cartitem.quantity += 1
    cartitem.save()
    cartitem.totalprice = cartitem.quantity * cartitem.products.product_price
    cartitem.save()
    return redirect("carts")

def DecreasecartQunatity(request,pk):
    cartitems = cart.objects.get(id =pk)
    if cartitems.quantity <1:
        cartitems.delete()
        return redirect("carts")
    else:
        cartitems.quantity -= 1
        cartitems.save()
        cartitems.totalprice = cartitems.quantity * cartitems.products.product_price
        cartitems.save()

    return redirect("carts")

def Increaseamount(requset,pk):
    cartitems = cart.objects.get(id = pk)
    cartitems.totalprice += 1
    cartitems.save()
    return redirect("carts")
    






    # let totalAmount = 0;

    #     function addItem(name, price) {
    #         const cartItems = document.getElementById('cart-items');

    #         const newItem = document.createElement('div');
    #         newItem.classList.add('cart-item');
    #         newItem.innerHTML = `
    #             <span>${name}</span>
    #             <span>$${price.toFixed(2)}</span>
    #         `;
    #         cartItems.appendChild(newItem);

    #         totalAmount += price;
    #         document.getElementById('total-amount').innerText = totalAmount.toFixed(2);
    #     }