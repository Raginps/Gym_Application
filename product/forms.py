from django.forms import ModelForm,TextInput,Select
from .models import productdetails
from .models import Myproteindetails


class productAddform(ModelForm):
    class Meta:
        model = productdetails
        fields = ["product_Name","product_Category","product_Description" ,"product_video"]


        widgets ={
            "product_Name":TextInput(attrs={"class":"form-control","placeholder":"product Name"}),
            "product_Category":Select(attrs={"class":"form-control","placeholder":"Category"}),

            }
        
class MyproteinAddform(ModelForm):
    class Meta:
        model = Myproteindetails
        fields = ["product_Name","product_Category","product_Description","product_image","product_price"]


        widgets ={
            "product_Name":TextInput(attrs={"class":"form-control","placeholder":"product Name"}),
            "product_Category":Select(attrs={"class":"form-control","placeholder":"Category"}),
            

            
            }
        


