from django.shortcuts import render
from django.views.generic import TemplateView
import datetime
import pytz
from django.db.models import Q
# from django.core.exceptions import ValidationError
# from django import forms

# from _user_panel.uaccounts.models import *
from _serviceprovider_panel.saccounts.models import *
from .forms import *

# Create your views here.
class CategoryManagementListView(TemplateView):
    def get(self,request,*args,**kwargs):

        # subcatlist = ServiceSubType.objects.all()
        catlist = ServiceType.objects.all()
        for c in catlist:
            q2 = ServiceSubType.objects.filter(type=c)
            c.subcatlist=q2

        # return render(request,'category_management/cat_list.html',{'subcatlist':subcatlist,'catlist':catlist})
        return render(request,'category_management/cat_list.html',{'catlist':catlist})

class CategoryManagementDateWiseListView(TemplateView):
    def get(self, request, *args, **kwargs):
        w1=request.GET.get('startdate')
        w2=request.GET.get('enddate')
        w1=w1.split('/')
        w2=w2.split('/')
        start_date = datetime.datetime(int(w1[2]), int(w1[0]), int(w1[1]), 0, 0, 0, 0, pytz.UTC)
        end_date = datetime.datetime(int(w2[2]), int(w2[0]), int(w2[1]), 23, 59, 59, 999999, pytz.UTC)

        print(start_date)
        print(end_date)
        # subcatlist=ServiceSubType.objects.filter(created_on__range=(start_date,end_date))

        catlist = ServiceType.objects.filter(created_on__range=(start_date,end_date))
        for c in catlist:
            q2 = ServiceSubType.objects.filter(type=c)
            c.subcatlist=q2

        return render(request,'category_management/cat_list.html',{'catlist':catlist})

class CategoryManagementAddCategoryView(TemplateView):
    def get(self,request,*args,**kwargs):
        return render(request,'category_management/add_category.html')
    def post(self,request,*args,**kwargs):
        form = CreateCategoryForm(data=request.POST or None,)
        x=0
        if form.is_valid():
            type = request.POST['catname']
            icon = request.FILES.get('caticon')
            print(icon.name)
            print(icon.size)
            print(icon.content_type)
            print(icon.name.split('.')[-1])
            if icon.size>1024000:
                x=1
            if icon.name.split('.')[-1].lower() not in ('png','jpg','jpeg'):
                x=1
            if x==1:
                return render(request,'category_management/add_category.html',{'form':form,'x':x})

            st = ServiceType(
                type=type,
                icon=icon,
            )
            st.save()
        return render(request,'category_management/add_category.html',{'form':form})

class CategoryManagementAddSubCategoryView(TemplateView):
    def get(self,request,*args,**kwargs):
        st=ServiceType.objects.all()
        return render(request,'category_management/add_subcategory.html',{'st':st})
    def post(self,request,*args,**kwargs):
        form = CreateSubCategoryForm(data=request.POST or None)
        st=ServiceType.objects.all()
        x=0
        if form.is_valid():
            subtype = request.POST['catname']
            icon = request.FILES.get('caticon')
            print(icon.name)
            print(icon.size)
            print(icon.content_type)
            print(icon.name.split('.')[-1])
            if icon.size>1024000:
                x=1
            if icon.name.split('.')[-1].lower() not in ('png','jpg','jpeg'):
                x=1
            if x==1:
                return render(request,'category_management/add_subcategory.html',{'st':st,'form':form,'x':x})

            type = request.POST['sty']
            type=ServiceType.objects.filter(type__iexact=type).first()
            sst = ServiceSubType(
                subtype=subtype,
                icon=icon,
                type=type,
            )
            sst.save()

        return render(request,'category_management/add_subcategory.html',{'st':st,'form':form})
