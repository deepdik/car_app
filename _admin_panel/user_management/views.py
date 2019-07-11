from django.shortcuts import render
from django.views.generic import TemplateView
import datetime
import pytz
from django.db.models import Q

from _user_panel.uaccounts.models import *
from _serviceprovider_panel.saccounts.models import *
# Create your views here.
class UserManagementListView(TemplateView):
    def get(self,request,*args,**kwargs):
        users = RegisteredUser.objects.filter(user_type__in=(1,2))
        return render(request,'user_management/user_list.html',{'users':users,'role':'0'})
    # template_name='user_management/user_list.html'
class UserManagementTypeWiseListView(TemplateView):
    def get(self,request,*args,**kwargs):
        role=self.kwargs['role']
        if role==3:
            users = RegisteredUser.objects.filter((Q(user_type=2) | Q(has_dual_account=True)) & Q(is_approved=False) & Q(user__is_active=True))
            return render(request,'user_management/user_list.html',{'users':users,'role':role})
        users = RegisteredUser.objects.filter(Q(user_type=role) | Q(has_dual_account=True))
        return render(request,'user_management/user_list.html',{'users':users,'role':role})

class UserManagementDateWiseListView(TemplateView):
    def get(self, request, *args, **kwargs):
        role=self.kwargs['role']

        w1=request.GET.get('startdate')
        w2=request.GET.get('enddate')
        w1=w1.split('/')
        w2=w2.split('/')
        start_date = datetime.datetime(int(w1[2]), int(w1[0]), int(w1[1]), 0, 0, 0, 0, pytz.UTC)
        end_date = datetime.datetime(int(w2[2]), int(w2[0]), int(w2[1]), 23, 59, 59, 999999, pytz.UTC)

        print(start_date)
        print(end_date)
        if role in ('1','2'):
            users  = RegisteredUser.objects.filter((Q(user_type=role) | Q(has_dual_account=True)) & Q(created_on__range=(start_date,end_date)))
        else:
            users  = RegisteredUser.objects.filter(Q(user_type__in=(1,2)) & Q(created_on__range=(start_date,end_date)))

        return render(request,'user_management/user_list.html',{'users':users,'role':role})

class UserManagementServiceProviderDetailView(TemplateView):
    def get(self,request,*args,**kwargs):
        pk=self.kwargs['pk']
        role=self.kwargs['role']
        userdata=RegisteredUser.objects.filter(id=pk).first()
        garagedata=Garage.objects.filter(user=userdata).first()
        categorydata=CategoryManager.objects.filter(garage=garagedata)
        scheduledata=WeeklySchedule.objects.filter(garage=garagedata)
        # print(garagedata.country)
        return render(request,'user_management/userprofile.html',{'userdata':userdata,'garagedata':garagedata,
                                                                    'categorydata':categorydata,
                                                                    'scheduledata':scheduledata,
                                                                })
    # template_name='user_management/userprofile.html'
