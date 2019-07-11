from rest_framework.generics import (ListAPIView,RetrieveAPIView)
from rest_framework.views import APIView
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

import logging
logger = logging.getLogger('accounts')

from .serializers import *
from _serviceprovider_panel.extra.models import *

class AboutUsView(APIView):
    # permission_classes=(IsAuthenticated,)
    # authentication_classes=(JSONWebTokenAuthentication,)
    def get(self,request,*args,**kwargs):
        logger.debug('About us get called')
        logger.debug(request.data)
        queryset=AboutUs.objects.all().first()
        data=AboutUsSerializer(queryset).data
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)

class TermsAndConditionView(APIView):
    # permission_classes=(IsAuthenticated,)
    # authentication_classes=(JSONWebTokenAuthentication,)
    def get(self,request,*args,**kwargs):
        logger.debug('Terms and condition get called')
        logger.debug(request.data)
        queryset=TermsAndCondition.objects.all().first()
        data=TermsAndConditionSerializer(queryset).data
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)

class HelpView(APIView):
    # permission_classes=(IsAuthenticated,)
    # authentication_classes=(JSONWebTokenAuthentication,)
    def get(self,request,*args,**kwargs):
        logger.debug('Help get called')
        logger.debug(request.data)
        queryset=Help.objects.all().first()
        data=HelpSerializer(queryset).data
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)

class LegalView(APIView):
    # permission_classes=(IsAuthenticated,)
    # authentication_classes=(JSONWebTokenAuthentication,)
    def get(self,request,*args,**kwargs):
        logger.debug('Legal get called')
        logger.debug(request.data)
        queryset=Legal.objects.all().first()
        data=LegalSerializer(queryset).data
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)

class PrivacyPolicyView(APIView):
    # permission_classes=(IsAuthenticated,)
    # authentication_classes=(JSONWebTokenAuthentication,)
    def get(self,request,*args,**kwargs):
        logger.debug('Privacy policy get called')
        logger.debug(request.data)
        queryset=PrivacyPolicy.objects.all().first()
        data=PrivacyPolicySerializer(queryset).data
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)

class FaqView(APIView):
    # permission_classes=(IsAuthenticated,)
    # authentication_classes=(JSONWebTokenAuthentication,)
    def get(self,request,*args,**kwargs):
        logger.debug('Faq get called')
        logger.debug(request.data)
        queryset=Faq.objects.all()
        data=FaqSerializer(queryset,many=True).data
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)

class NotificationView(APIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    def get(self,request,*args,**kwargs):
        logger.debug('Notification get called')
        logger.debug(request.data)
        user=request.user.ruser

        queryset=Notification.objects.filter(user__id=user.id).distinct()

        data=NotificationSerializer(queryset,many=True).data
        return Response({
            'message':'data retrieved successfully',
            'success':'True',
            'data':data,
        },status=HTTP_200_OK,)
