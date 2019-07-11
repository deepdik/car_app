from django.views.generic import TemplateView
from rest_framework.views import (APIView,)
from rest_framework.generics import (ListAPIView,RetrieveAPIView,)
from rest_framework.permissions import (IsAuthenticated,)
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import  JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import (
                                        HTTP_200_OK,
                                    	HTTP_400_BAD_REQUEST,
                                    	HTTP_204_NO_CONTENT,
                                    	HTTP_201_CREATED,
                                    	HTTP_500_INTERNAL_SERVER_ERROR,
                                    )
from django.db.models import Q

import logging
logger = logging.getLogger('accounts')

from .serializers import *

class ServiceTypeListView(ListAPIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)

    def get(self,request,*args,**kwargs):
        logger.debug('service type list get called')
        logger.debug(request.data)
        queryset=ServiceType.objects.all()
        serializer=ServiceTypeListSerializer(queryset,many=True,context={'request':request,})
        data=serializer.data
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK)

class ServiceSubTypeListView(ListAPIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    def get(self,request,*args,**kwargs):
        logger.debug('service subtype get called')
        logger.debug(request.data)
        pk=self.kwargs['pk']
        queryset=ServiceSubType.objects.filter(type__id=pk)

        serializer=ServiceSubTypeSerializer(queryset,many=True,context={'request':request})
        data=serializer.data
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)

class GarageListView(ListAPIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    def get(self,request,*args,**kwargs):
        logger.debug('service subtype get called')
        logger.debug(request.data)
        pk=self.kwargs['pk']
        # sst=ServiceSubType.objects.filter(id=pk).first()
        queryset=Garage.objects.filter(service_subtype__id=pk).distinct()
        serializer=GarageListSerializer(queryset,many=True,context={'request':request})
        data=serializer.data
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

class GarageDetailView(RetrieveAPIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    def get(self,request,*args,**kwargs):
        pk=self.kwargs['pk']
        queryset=Garage.objects.filter(id=pk)
        serializer=GarageAllDetailSerializer(queryset,many=True,context={'request':request})
        data=serializer.data
        return Response({
            'message':'data retrieved successfully',
            'success':'False',
            'data':data,
        },status=HTTP_200_OK,)

class GarageOfferDetailView(APIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    def get(self,request,*args,**kwargs):
        logger.debug('Offer detail get called')
        logger.debug(request.data)
        pk=self.kwargs['pk']
        queryset=Offer.objects.filter(id=pk).first()
        garage=queryset.garage.name
        serializer=GarageOfferDetailSerializer(queryset,context={'garage':garage})
        data=serializer.data
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)

class UserReviewView(APIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    def post(self,request,*args,**kwargs):
        id=self.kwargs['pk']
        serializer=UserReviewSerializer(data=request.data,context={'request':request,'id':id})
        if serializer.is_valid():
            serializer.save()
            data=serializer.data
            return Response({
                'message':'data submitted successfully',
                'success':'True',
                'data':data,
            },status=HTTP_200_OK,)
        return Response({
            'message':'failed to submit',
            'success':'False',
            'data':serializer.errors,
        },status=HTTP_200_OK,)
