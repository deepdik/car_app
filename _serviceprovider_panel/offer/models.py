from django.db import models
from datetime import datetime
# Create your models here.
from _serviceprovider_panel.saccounts.models import *

class Offer(models.Model):
    garage=models.ForeignKey(Garage,on_delete=models.CASCADE,related_name='ogarage')
    image1=models.ImageField(upload_to='serviceprovider/offer/image',blank=True,null=True)
    image2=models.ImageField(upload_to='serviceprovider/offer/image',blank=True,null=True)
    image3=models.ImageField(upload_to='serviceprovider/offer/image',blank=True,null=True)
    image4=models.ImageField(upload_to='serviceprovider/offer/image',blank=True,null=True)
    video1=models.FileField(upload_to='serviceprovider/offer/video',blank=True,null=True)
    video2=models.FileField(upload_to='serviceprovider/offer/video',blank=True,null=True)
    title=models.CharField(max_length=100,)
    description=models.CharField(max_length=500,)
    coupon=models.CharField(max_length=10,)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    # is_active=models.BooleanField(default=True)
    def is_active(self):
        if end_date>datetime.now():
            return False
        return True

    def __str__(self):
        return self.title


class SubscriptionPlan(models.Model):
    plan_name=models.CharField(max_length=100,)
    plan_desc=models.CharField(max_length=800,)
    price=models.DecimalField(max_digits=10,decimal_places=2,default='0.00',)
    validity_from=models.DateField(auto_now_add=False,)
    validity_to=models.DateField(auto_now_add=False,)
    created_on=models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.plan_name

class UserSubscription(models.Model):
    plan=models.ForeignKey(SubscriptionPlan,on_delete=models.CASCADE,related_name='us_plan')
    ruser=models.ForeignKey(RegisteredUser,on_delete=models.CASCADE,related_name='us_ruser')
    created_on=models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.plan.title+'-'+self.ruser.first_name+'-'+self.ruser.last_name
