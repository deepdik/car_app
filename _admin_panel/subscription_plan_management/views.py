from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
import pytz
from django.db.models import Q

from _serviceprovider_panel.offer.models import *
from .forms import *

class SubscriptionPlanListView(TemplateView):
    def get(self,request,*args,**kwargs):
        sublist=SubscriptionPlan.objects.all()
        return render(request,'subscription_plan_management/user_subscription_list.html',{'sublist':sublist})

class SubscriptionPlanDateWiseListView(TemplateView):
    def get(self, request, *args, **kwargs):
        w1=request.GET.get('startdate')
        w2=request.GET.get('enddate')
        w1=w1.split('/')
        w2=w2.split('/')
        start_date = datetime(int(w1[2]), int(w1[0]), int(w1[1]), 0, 0, 0, 0, pytz.UTC)
        end_date = datetime(int(w2[2]), int(w2[0]), int(w2[1]), 23, 59, 59, 999999, pytz.UTC)

        print(start_date)
        print(end_date)

        sublist = SubscriptionPlan.objects.filter(created_on__range=(start_date,end_date))

        return render(request,'subscription_plan_management/user_subscription_list.html',{'sublist':sublist})

class AddNewSubscriptionView(TemplateView):
    def get(self,request,*args,**kwargs):
        return render(request,'subscription_plan_management/add_new_subscription.html')
    def post(self,request,*args,**kwargs):
        form=CheckAddNewSubPlanForm(data=request.POST or None)
        pname=request.POST['pname']
        pdesc=request.POST['pdesc']
        price=request.POST['price']
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']
        if form.is_valid():
            startdate = datetime.strptime(startdate, '%m/%d/%Y').strftime('%Y-%m-%d')
            enddate = datetime.strptime(enddate, '%m/%d/%Y').strftime('%Y-%m-%d')

            sp=SubscriptionPlan(
                plan_name=pname,
                plan_desc=pdesc,
                price=price,
                validity_from=startdate,
                validity_to=enddate,
            )
            sp.save()
            return render(request,'subscription_plan_management/add_new_subscription.html',{'form':form})
        context={}
        context['pname']=pname
        context['pdesc']=pdesc
        context['price']=price
        context['startdate']=startdate
        context['enddate']=enddate
        return render(request,'subscription_plan_management/add_new_subscription.html',{'context':context,'form':form})
