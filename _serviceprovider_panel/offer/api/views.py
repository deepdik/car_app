from rest_framework.views import (APIView,)
from rest_framework.generics import (CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,)
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
from datetime import datetime
from django.utils.timezone import utc
from datetime import date
#
from .serializers import *
from _serviceprovider_panel.offer.models import *
from _serviceprovider_panel.saccounts.models import *

import logging
logger = logging.getLogger('accounts')

class CreateOfferView(CreateAPIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    def post(self,request,*args,**kwargs):
        logger.debug('Create offer post called')
        logger.debug(request.data)
        ruser=request.user.ruser
        garage=Garage.objects.filter(user=ruser).first()
        serializer=CreateOfferSerializer(data=request.data,context={'request':request,'garage':garage})
        if serializer.is_valid():
            serializer.save()
            data=serializer.data
            return Response({
                'message':'data saved successfully',
                'success':'True',
                'data':data,
            },status=HTTP_200_OK,)
        else:
            return Response({
                'message':'data save failed',
                'success':'False',
                'data':serializer.errors,
            },status=HTTP_400_BAD_REQUEST,)

class GarageWiseOfferListView(ListAPIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    serializer_class=GarageWiseOfferListSerializer

    def get(self,request,*args,**kwargs):
        logger.debug('Garage wise offer list get called')
        logger.debug(request.data)
        ruser=self.request.user.ruser
        garage=Garage.objects.filter(user=ruser).first()
        queryset=Offer.objects.filter(garage=garage)
        serializer=GarageWiseOfferListSerializer(queryset,many=True,context={'request':request})
        data=serializer.data
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)

class ActiveOfferListView(ListAPIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    serializer_class=GarageWiseOfferListSerializer

    def get(self,request,*args,**kwargs):
        logger.debug('all offer list get called')
        logger.debug(request.data)
        # ruser=self.request.user.ruser
        # garage=Garage.objects.filter(user=ruser).first()
        now = datetime.utcnow().replace(tzinfo=utc)
        queryset=Offer.objects.filter(end_date__lte=now)
        serializer=GarageWiseOfferListSerializer(queryset,many=True,context={'request':request})
        data=serializer.data
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)

class OfferDetailView(RetrieveAPIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)

    def get(self,request,*args,**kwargs):
        logger.debug('Offer detail get called')
        logger.debug(request.data)
        pk=self.kwargs['pk']
        queryset=Offer.objects.filter(id=pk).first()
        serializer=OfferDetailSerializer(queryset,context={'request':request,})
        data=serializer.data
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)

class OfferUpdateView(UpdateAPIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    def post(self,request,*args,**kwargs):
        logger.debug('Create offer post called')
        logger.debug(request.data)
        pk=self.kwargs['pk']
        offer=Offer.objects.filter(id=pk).first()
        serializer=OfferUpdateSerializer(data=request.data,context={'request':request,'offer':offer})
        if serializer.is_valid():
            serializer.save()
            data=serializer.data
            return Response({
                'message':'data saved successfully',
                'success':'True',
                'data':data,
            },status=HTTP_200_OK,)
        else:
            return Response({
                'message':'data save failed',
                'success':'False',
                'data':serializer.errors,
            },status=HTTP_400_BAD_REQUEST,)

class OfferDeleteView(DestroyAPIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)

    def get(self,request,*args,**kwargs):
        logger.debug('Create offer post called')
        logger.debug(request.data)
        pk=self.kwargs['pk']
        Offer.objects.filter(id=pk).delete()
        return Response({
            'message':'data deleted successfully',
            'success':'True',
        },status=HTTP_200_OK,)

class SubPlanListView(ListAPIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    serializer_class=SubPlanListSerializer

    def get(self,request,*args,**kwargs):
        logger.debug('Subscription plan list get called')
        logger.debug(request.data)
        queryset=SubscriptionPlan.objects.filter(validity_to__gte=date.today())
        serializer=SubPlanListSerializer(queryset,many=True,context={'request':request})
        data=serializer.data
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)
