from django.urls import path
from .import views


urlpatterns=[
    path("Myproducts",views.Myproducts,name="Myproducts"),
    path("Myprotein",views.Myprotein,name="Myprotein"),
    path("proteinsingleview/<int:pk>",views.proteinsingleview,name="proteinsingleview")
   

]