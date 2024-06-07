from django.urls import path
from.import views

urlpatterns = [
    path("",views.Index,name="Index"),
    path("singIn",views.singIn,name="singIn"),
    path("signUp",views.signUp,name="signUp"),
    path("signout",views.signout,name="signout"),
    path("userIndex",views.userIndex,name="userIndex"),
    path("Home",views.Home,name="Home"),
    path("workout",views.workout,name="workout"),
    path("about",views.about,name="about"),
    path("team",views.team,name="team"),
    path("contact",views.contact,name="contact"),
    path("blog",views.blog,name="blog"),
    path("detail",views.detail,name="detail"),
    path("testimonial",views.testimonial,name="testimonial"),
    path("merchant",views.merchant,name="merchant"),
    path("deleteworkout/<int:pk>", views.deleteworkout, name="deleteworkout"),
    path("protein",views.protein,name="protein"),
    path("proteinpowder",views.proteinpowder,name="proteinpowder"),
    path("proteinsingleview/<int:pk>",views.proteinsingleview,name="proteinsingleview"),
    path("deleteprotein/<int:pk>", views.deleteprotein, name="deleteprotein"),
    path("AddToCart/<int:pk>", views.AddToCart, name="AddToCart"),
    path("carts",views.carts,name="carts"),
    path("deletecart/<int:pk>", views.deletecart, name="deletecart"),
    path("IncreaseCartQuantity/<int:pk>", views.IncreaseCartQuantity, name="IncreaseCartQuantity"),
    path("DecreasecartQunatity/<int:pk>", views.DecreasecartQunatity, name="DecreasecartQunatity"),
    path("Increaseamount/<int:pk>", views.Increaseamount, name="Increaseamount"),
    path("commentsection/<int:pk>", views.commentsection, name="commentsection"),
    path("Comment/<int:pk>", views.Comments, name="Comment"),
    path("customercoment/<int:pk>", views.customercoment, name="customercoment"),
    path("customercomentsection/<int:pk>", views.customercomentsection, name="customercomentsection"),


    









]