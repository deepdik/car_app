from django.shortcuts import render
from django.views.generic import TemplateView
# import datetime
import pytz
from datetime import datetime

# from django.core.exceptions import ValidationError
# from django import forms

# from _user_panel.uaccounts.models import *
from _serviceprovider_panel.extra.models import *
from .forms import *

class NotificationManagementCreateView(TemplateView):
    def get(self,request):
        users = RegisteredUser.objects.filter(user_type__in=(1,2),user__is_active=True)
        return render(request,'notification_management/send_notification.html',{'users':users,'role':'0'})

    def post(self,request,*args,**kwargs):
        nottitle=request.POST['nottitle']
        notdesc=request.POST['notdesc']
        form = UnknownForm(request.POST)
        if form.is_valid():
            for item in form.cleaned_data['select']:
                ruser=RegisteredUser.objects.filter(id=item.id).first()
                n=Notification(
                    title=nottitle,
                    description=notdesc,
                )
                n.save()
                un=UserNotification(
                    notification=n,
                    user=ruser,
                )
                un.save()
                print('data saved successfully')
        else:
            print(form.errors)

        users = RegisteredUser.objects.filter(user_type__in=(1,2),user__is_active=True)
        return render(request,'notification_management/send_notification.html',{'users':users,'role':'0','message':'Notifications sent successfully.'})

# class NotificationManagementUserListView(TemplateView):
#     def get(self,request,*args,**kwargs):
#         users = RegisteredUser.objects.filter(user_type__in=(1,2),user__is_active=True)
#         return render(request,'notification_management/add_user.html',{'users':users,'role':'0'})

class NotificationManagementUserTypeWiseListView(TemplateView):
    def get(self,request,*args,**kwargs):
        role=self.kwargs['role']
        users = RegisteredUser.objects.filter(user_type=role,user__is_active=True)
        return render(request,'notification_management/send_notification.html',{'users':users,'role':role})

class NotificationManagementUserDateWiseListView(TemplateView):
    def get(self, request, *args, **kwargs):
        role=self.kwargs['role']

        w1=request.GET.get('startdate')
        w2=request.GET.get('enddate')
        w1=w1.split('/')
        w2=w2.split('/')
        start_date = datetime(int(w1[2]), int(w1[0]), int(w1[1]), 0, 0, 0, 0, pytz.UTC)
        end_date = datetime(int(w2[2]), int(w2[0]), int(w2[1]), 23, 59, 59, 999999, pytz.UTC)

        print(start_date)
        print(end_date)
        if role in ('1','2'):
            users  = RegisteredUser.objects.filter(user_type=role,user__is_active=True,created_on__range=(start_date,end_date))
        else:
            users  = RegisteredUser.objects.filter(user_type__in=(1,2),user__is_active=True,created_on__range=(start_date,end_date))

        return render(request,'notification_management/send_notification.html',{'users':users,'role':role})
