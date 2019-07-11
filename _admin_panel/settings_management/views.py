from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
import datetime
import pytz
from django.db.models import Q
# from django.core.exceptions import ValidationError
# from django import forms

# from _user_panel.uaccounts.models import *
from _serviceprovider_panel.extra.models import *
from .forms import *

# Create your views here.

class SettingsManagementListView(TemplateView):
    def get(self,request,*args,**kwargs):
        opts=NewOptions.objects.all()
        return render(request,'settings_management/settings_list.html',{'opts':opts})

# class SettingsManagementDisplayView(View):


class SettingsManagementEditView(View):
    def get(self,request,*args,**kwargs):
        id=self.kwargs['id']
        if id=='f1':
            context=AboutUs.objects.all().first()
        elif id=='f2':
            context=TermsAndCondition.objects.all().first()
        elif id=='f3':
            context=Faq.objects.all().first()
        elif id=='f4':
            context=Help.objects.all().first()
        elif id=='f5':
            context=PrivacyPolicy.objects.all().first()
        elif id=='f6':
            context=Legal.objects.all().first()
        else:
            context=NewOptions.objects.filter(id=id).first()
        return render(request,'settings_management/edit_option.html',{'context':context,'id':id})

    def post(self,request,*args,**kwargs):
        id=self.kwargs['id']
        # servicetitle=request.POST['servicetitle']
        servicedesc=request.POST['servicedesc']
        # form=SettingsManagementEditForm()
        if id=='f1':
            obj=AboutUs.objects.all().first()
            obj.content=servicedesc
            obj.save()
        elif id=='f2':
            obj=TermsAndCondition.objects.all().first()
            obj.content=servicedesc
            obj.save()
        elif id=='f3':
            obj=Faq.objects.all().first()
            obj.content=servicedesc
            obj.save()
        elif id=='f4':
            obj=Help.objects.all().first()
            obj.content=servicedesc
            obj.save()
        elif id=='f5':
            obj=PrivacyPolicy.objects.all().first()
            obj.content=servicedesc
            obj.save()
        elif id=='f6':
            obj=Legal.objects.filterall().first()
            obj.content=servicedesc
            obj.save()
        else:
            obj=NewOptions.objects.filter(id=id).first()
            obj.content=servicedesc
            obj.save()
        opts=NewOptions.objects.all()
        return render(request,'settings_management/edit_option.html',{'context':obj,'id':id})

class SettingsManagementAddView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'settings_management/create_new_option.html')
    def post(self,request,*args,**kwargs):
        title=request.POST['opttitle']
        content=request.POST['optcontent']
        nopt=NewOptions(
            title=title,
            content=content,
        )
        nopt.save()
        opts=NewOptions.objects.all()
        return render(request,'settings_management/create_new_option.html')
