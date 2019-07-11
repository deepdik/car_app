from django.urls import path

from .views import *

app_name='up_search'

urlpatterns=[
    path('list/',HomeSearchView.as_view(),name='up_search'),
    path('popular/garage/',PopularGarageSearchView.as_view(),name='up_popular_garage'),
    path('popular/category/',PopularCategorySearchView.as_view(),name='up_popular_category'),
]
