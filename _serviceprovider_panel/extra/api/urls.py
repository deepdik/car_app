from django.urls import path

from .views import *

app_name='spp_extra'

urlpatterns=[
    path('aboutus/',AboutUsView.as_view(),name='spp_aboutus'),
    path('termsandcondition/',TermsAndConditionView.as_view(),name='spp_termsandcondition'),
    path('help/',HelpView.as_view(),name='spp_help'),
    path('legal/',LegalView.as_view(),name='spp_leagl'),
    path('privacypolicy/',PrivacyPolicyView.as_view(),name='spp_privacy_policy'),
    path('faq/',FaqView.as_view(),name='spp_faq'),
    path('notification/',NotificationView.as_view(),name='spp_notification'),
]
