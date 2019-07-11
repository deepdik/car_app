from django.db import models
from django.utils.text import slugify
# import pytz
# from datetime import datetime
from django.utils import timezone

from _user_panel.uaccounts.models import RegisteredUser

# Create your models here.
days_choices=(('1','sat'),('2','sun'),('3','mon'),('4','tue'),('5','wed'),('6','thur'),('7','fri'))

# default=timezone.now
class ServiceType(models.Model):
    type=models.CharField(max_length=50)
    icon=models.ImageField(upload_to='serviceprovider/service_type',blank=True,null=True)
    slug = models.SlugField(unique=True,default='')
    created_on = models.DateTimeField(auto_now_add=True)
    # created_on = models.DateTimeField(default=timezone.now)
    category_rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.type

    def save(self, *args, **kwargs):
        self.slug = slugify(self.type)
        super(ServiceType, self).save(*args, **kwargs)

class ServiceSubType(models.Model):
    subtype=models.CharField(max_length=50)
    type=models.ForeignKey(ServiceType,on_delete=models.CASCADE)
    icon=models.ImageField(upload_to='serviceprovider/service_subtype',blank=True,null=True)
    slug = models.SlugField(unique=True,default='')
    created_on = models.DateTimeField(auto_now_add=True)
    subcategory_rating = models.PositiveIntegerField(default=0)
    # created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subtype

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subtype)
        super(ServiceSubType, self).save(*args, **kwargs)

class Garage(models.Model):
    name=models.CharField(max_length=50,)
    store_image1=models.ImageField(upload_to='serviceprovider/garage', blank=True,null=True)
    store_image2=models.ImageField(upload_to='serviceprovider/garage', blank=True,null=True)
    store_image3=models.ImageField(upload_to='serviceprovider/garage', blank=True,null=True)
    contact_person=models.CharField(max_length=70)

    lat=models.CharField(max_length=20,)
    lon=models.CharField(max_length=20,)
    location=models.CharField(max_length=500,)
    state=models.CharField(max_length=20,)
    city=models.CharField(max_length=20,)
    country=models.CharField(max_length=20,)
    country_code=models.CharField(max_length=10)
    contact_num=models.CharField(max_length=15,)

    tax_registration_num=models.CharField(max_length=50,blank=True,null=True)
    tax_registration_date=models.DateTimeField(blank=True,null=True)

    created_on=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    is_owner=models.BooleanField(default=True)
    user=models.ForeignKey(RegisteredUser,on_delete=models.CASCADE,related_name='guser')
    service_type=models.ManyToManyField(ServiceType,related_name='gst', through='CategoryManager')
    service_subtype=models.ManyToManyField(ServiceSubType,related_name='gsst', through='SubCategoryManager')

    garage_rating=models.PositiveIntegerField(default=0,)

    slug1 = models.SlugField(default='')
    slug2 = models.SlugField(default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug1 = slugify(self.name)
        self.slug2 = slugify(self.location)
        super(Garage, self).save(*args, **kwargs)

class CategoryManager(models.Model):
    garage=models.ForeignKey(Garage,on_delete=models.CASCADE,related_name='cm_garage')
    category=models.ForeignKey(ServiceType,on_delete=models.CASCADE,related_name='cm_category')
    class Meta:
        unique_together=('garage','category')
    def __str__(self):
        return str(self.garage)+' '+str(self.category)

class SubCategoryManager(models.Model):
    garage=models.ForeignKey(Garage,on_delete=models.CASCADE,related_name='scm_garage')
    subcategory=models.ForeignKey(ServiceSubType,on_delete=models.CASCADE,related_name='scm_subcategory')
    class Meta:
        unique_together=('garage','subcategory')
    def __str__(self):
        return str(self.garage)+' '+str(self.subcategory)

class WeeklySchedule(models.Model):
    garage=models.ForeignKey(Garage,on_delete=models.CASCADE,related_name='wsgarage')
    day=models.CharField(max_length=10,choices=days_choices)
    start_time=models.CharField(max_length=10)
    end_time=models.CharField(max_length=10)

    def __str__(self):
        return self.garage.name

class UserReview(models.Model):
    garage=models.ForeignKey(Garage,on_delete=models.CASCADE,related_name='rvgarage')
    user=models.ForeignKey(RegisteredUser,on_delete=models.CASCADE,related_name='rvuser')
    review=models.CharField(max_length=200,)
    rating=models.PositiveIntegerField(default=0)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review

class CustomerComplaint(models.Model):
    user=models.ForeignKey(RegisteredUser,on_delete=models.CASCADE,related_name='csuser')
    name=models.CharField(max_length=50,)
    email=models.CharField(max_length=80,)
    complaint=models.CharField(max_length=200,)

    def __str__(self):
        return self.user.first_name

class TempGarageImage(models.Model):
    user=models.ForeignKey(RegisteredUser,on_delete=models.CASCADE,related_name='tgi_user')
    image=models.ImageField(upload_to='serviceprovider/temp', blank=True)
    def __str__(self):
        return self.user.first_name
