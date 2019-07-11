from django import forms
from django.contrib.auth.models import User

from _serviceprovider_panel.saccounts.models import *

# from accounts.models import *

class CreateCategoryForm(forms.Form):
    def clean(self):
        type=self.data['catname']
        if not type or type=="":
            raise forms.ValidationError('Please provide category name')
        st_obj=ServiceType.objects.filter(type=type).first()
        if st_obj:
            raise forms.ValidationError('This category already exists')



class CreateSubCategoryForm(forms.Form):
    def clean(self):
        type=self.data['sty']
        subtype=self.data['catname']

        if not subtype or subtype=="":
            raise forms.ValidationError('Please provide subcategory name')
        if not type or type=="":
            raise forms.ValidationError('Please select category')
        st_obj=ServiceType.objects.filter(type=type).first()
        sst_obj=ServiceSubType.objects.filter(type=st_obj,subtype=subtype).first()
        if sst_obj:
            raise forms.ValidationError('This subcategory under this category already exists')
