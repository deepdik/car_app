from django import forms
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User

from _serviceprovider_panel.saccounts.models import *

class CheckAddNewSubPlanForm(forms.Form):
    def clean(self):
        pname=self.data['pname']
        pdesc=self.data['pdesc']
        price=self.data['price']
        startdate=self.data['startdate']
        enddate=self.data['enddate']

        startdate = datetime.strptime(startdate, '%m/%d/%Y').strftime('%Y-%m-%d')
        startdate = datetime.strptime(startdate, '%Y-%m-%d').date()
        enddate = datetime.strptime(enddate, '%m/%d/%Y').strftime('%Y-%m-%d')

        if not pname or pname == "":
            raise forms.ValidationError('Please provide plan name')
        if not pdesc or pdesc == "":
            raise forms.ValidationError('Please provide plan description')
        if not price or price == "":
            raise forms.ValidationError('Please provide price')
        if not startdate or startdate == "":
            raise forms.ValidationError('Please provide from date')
        if not enddate or enddate == "":
            raise forms.ValidationError('Please provide to date')

        price=price.split('.')
        if len(price) >2:
            raise forms.ValidationError('Please provide a valid price')
        pr=''
        for i in price:
            pr=pr+i
        if not pr.isdigit():
            raise forms.ValidationError('Please provide a valid price')
        if len(pr)>10:
            raise forms.ValidationError('Price is too high. Total 10 digits are possible including decimal.')
        if len(price)==2:
            if len(price[1])>2:
                raise forms.ValidationError('Please provide a valid price')

        if startdate<date.today():
            raise forms.ValidationError('From date can not be less than today')
