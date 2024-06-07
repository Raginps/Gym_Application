from django.db import models
from django.contrib.auth.models import User

class productdetails(models.Model):

    options =(("full body workout","full body workout"),("Yoga Flow with an Exercise Ball","Yoga Flow with an Exercise Ball"),("Bed Exercises","Bed Exercises"),("Home Workout","Home Workout"),("Yoga in Bed","Yoga in Bed"))
    product_Name = models.CharField(max_length= 225)
    product_Category = models.CharField(max_length = 255,choices =options)
    product_Description = models.CharField(max_length = 1000)
    product_video = models.FileField(upload_to='product_video')
    merchant = models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank=True)


class Myproteindetails(models.Model):
    CATEGORY_CHOICES = (("Optimum Nutrition Protein Supplement","Optimum Nutrition Protein Supplement"),("Nutrition Protein Supplement","Nutrition Protein Supplement "))

       

    product_Category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)    
    product_Name = models.CharField(max_length= 225)
    # product_Category = models.CharField(max_length = 255,choices =options)
    product_Description = models.CharField(max_length = 1000)
    product_image = models.FileField(upload_to="product_image")
    product_price = models.FloatField(max_length= 225 )
    merchant = models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.product_Name
    
class cart(models.Model):
    products = models.ForeignKey(Myproteindetails,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    totalprice =models.FloatField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.cart}'


class Comment(models.Model):
    video = models.ForeignKey(productdetails,on_delete=models.CASCADE,related_name='comments')
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class usercoment(models.Model):
    protein =models.ForeignKey(Myproteindetails,on_delete=models.CASCADE,related_name='comments')
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

    