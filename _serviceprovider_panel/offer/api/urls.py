from django.urls import path

from .views import *

app_name='spp_offer'

urlpatterns=[
    path('create/',CreateOfferView.as_view(),name='spp_creare'),
    path('offers/',GarageWiseOfferListView.as_view(),name='spp_offers'),
    path('active_offers/',ActiveOfferListView.as_view(),name='spp_active_offers'),
    path('offers/<int:pk>',OfferDetailView.as_view(),name='spp_offer_detail'),
    path('update/<int:pk>',OfferUpdateView.as_view(),name='spp_offer_update'),
    path('delete/<int:pk>',OfferDeleteView.as_view(),name='spp_offer_delete'),
    path('sub_plan_list/',SubPlanListView.as_view(),name='spp_sub_plan_list'),
]
