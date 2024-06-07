from django.shortcuts import render,HttpResponse,redirect


def AdminDecorator(func):
    def wrapper_fun(requset,*args,**kwargs):
        group =None
        if requset.user.groups.all().exists():
            group = requset.user.groups.all()[0].name
        if group == "user":
            return redirect("userIndex")
        if group == "merchant":
            return func(requset,*args,**kwargs)
        if group == None: 
            return redirect("userIndex")
    return wrapper_fun