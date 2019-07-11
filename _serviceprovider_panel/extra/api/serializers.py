from rest_framework import serializers
from rest_framework.exceptions import APIException

from _serviceprovider_panel.extra.models import *

class APIException400(APIException):
    satus_code=400

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AboutUs
        fields='__all__'

class TermsAndConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model=TermsAndCondition
        fields='__all__'

class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Help
        fields='__all__'

class LegalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Legal
        fields='__all__'

class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model=PrivacyPolicy
        fields='__all__'

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model=Faq
        fields='__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=('title','description','created_on')
