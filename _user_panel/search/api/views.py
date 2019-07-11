from django.db.models import Q
from rest_framework.filters import (SearchFilter,OrderingFilter,)
from rest_framework.generics import (CreateAPIView,GenericAPIView,ListAPIView,)
from rest_framework.views import (APIView)
from django.views.generic import TemplateView

from django.contrib.auth.models import User
from rest_framework.permissions import (AllowAny,IsAuthenticated,)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import (
                                        HTTP_200_OK,
                                    	HTTP_400_BAD_REQUEST,
                                    	HTTP_204_NO_CONTENT,
                                    	HTTP_201_CREATED,
                                    	HTTP_500_INTERNAL_SERVER_ERROR,
                                )
from rest_framework_jwt.authentication import  JSONWebTokenAuthentication

from .serializers import *
from _user_panel.ugarage.api.serializers import GarageListSerializer,ServiceTypeListSerializer
from _serviceprovider_panel.saccounts.models import *

import logging
logger = logging.getLogger('accounts')


class HomeSearchView(ListAPIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    serializer_class=GarageListSerializer
    filter_backends=(SearchFilter,OrderingFilter,)
    search_fields=['slug1','slug2','state','city','country','service_type','service_subtype',]

    def get_queryset(self,*args,**kwargs):
        queryset_list=Garage.objects.all() ## find most popular garages here
        query=self.request.GET.get('q',None)

        print('----------------')
        print(query)
        st=ServiceType.objects.filter(slug__icontains=query)
        sst=ServiceSubType.objects.filter(slug__icontains=query)
        if query:
            queryset_list=queryset_list.filter(
                Q(name__icontains=query)|
                Q(location__icontains=query)|
                Q(state__icontains=query)|
                Q(city__icontains=query)|
                Q(country__icontains=query)|
                Q(service_type__in=(st))|
                Q(service_subtype__in=(sst))
            ).distinct()
        return queryset_list
    def list(self,*args,**kwargs):
        logger.debug('home search list called')
        logger.debug(self.request.data)
        qs=self.get_queryset()
        data=GarageListSerializer(qs,many=True,context={'request':self.request}).data
        for obj in data:
            if obj['is_favorite']=='True':
                obj['make_fav_garage_url']=''
            else:
                obj['remove_fav_garage_url']=''
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)

class PopularGarageSearchView(ListAPIView):
    permisstion_class=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    serializer_class=GarageListSerializer
    filter_backends=(SearchFilter,OrderingFilter,)

    def get_queryset(self,*args,**kwargs):
        queryset=Garage.objects.filter(garage_rating__gte=4)
        return queryset

    def list(self,request,*args,**kwargs):
        logger.debug('popular garage search list called')
        logger.debug(self.request.data)
        qs=self.get_queryset()
        data=GarageListSerializer(qs,many=True,context={'request':self.request}).data
        for obj in data:
            if obj['is_favorite']=='True':
                obj['make_fav_garage_url']=''
            else:
                obj['remove_fav_garage_url']=''
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)

class PopularCategorySearchView(ListAPIView):
    permisstion_class=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    serializer_class=ServiceTypeListSerializer
    filter_backends=(SearchFilter,OrderingFilter,)

    def get_queryset(self,*args,**kwargs):
        # Employer.objects.values('id').annotate(jobtitle_count=Count('jobtitle')).order_by('-jobtitle_count')[:5]
        queryset=ServiceType.objects.all().order_by('-category_rating')[:10]
        return queryset

    def list(self,request,*args,**kwargs):
        logger.debug('popular category search list called')
        logger.debug(self.request.data)
        qs=self.get_queryset()
        data=ServiceTypeListSerializer(qs,many=True,context={'request':self.request}).data

        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)
