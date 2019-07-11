"""Carmention URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from _user_panel.uaccounts.views import activate

urlpatterns = [
    path('admin/', admin.site.urls),

    #Email varification
    url('^', include('django.contrib.auth.urls')),
    #User Panel
    path('user/',include('_user_panel.uaccounts.api.urls',namespace='up_accounts')),
    path('user/detail/',include('_user_panel.ugarage.api.urls',namespace='up_garage')),
    path('user/search/',include('_user_panel.search.api.urls',namespace='up_search')),

    #Email Activation
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',activate, name='activate'),
    #Service Provider Panel
    path('serviceprovider/',include('_serviceprovider_panel.saccounts.api.urls',namespace='spp_accounts')),
    path('serviceprovider/offer/',include('_serviceprovider_panel.offer.api.urls',namespace='spp_offer')),
    path('serviceprovider/extra/',include('_serviceprovider_panel.extra.api.urls',namespace='spp_extra')),

    #Admin Panel
    path('carmension_admin/',include('_admin_panel.aaccounts.urls', namespace='ap_accounts')),
    path('user_management/',include('_admin_panel.user_management.urls', namespace='ap_user_mgmt')),
    path('category_management/',include('_admin_panel.category_management.urls', namespace='ap_cat_mgmt')),
    path('settings_management/',include('_admin_panel.settings_management.urls', namespace='ap_set_mgmt')),
    path('notification_management/',include('_admin_panel.notification_management.urls', namespace='ap_not_mgmt')),
    path('subscription_plan_management/',include('_admin_panel.subscription_plan_management.urls', namespace='ap_splan_mgmt')),

    #Admin Panel Different APIs
    path('ap_um_api/', include('_admin_panel.user_management.api.urls', namespace='ap_um_api')),
    path('ap_cm_api/', include('_admin_panel.category_management.api.urls', namespace='ap_cm_api')),
    path('ap_setm_api/', include('_admin_panel.settings_management.api.urls', namespace='ap_setm_api')),
    path('ap_notm_api/', include('_admin_panel.notification_management.api.urls', namespace='ap_notm_api')),
    path('ap_splanm_api/', include('_admin_panel.subscription_plan_management.api.urls', namespace='ap_splanm_api')),
    url(r'^silk', include('silk.urls', namespace='silk'))

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
