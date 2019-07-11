from rest_framework import serializers
from rest_framework.exceptions import APIException
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from django.conf import settings
from datetime import datetime
from django.db.models import Sum

from _serviceprovider_panel.saccounts.models import *
from _user_panel.uaccounts.models import RegisteredUser,FavoriteGarage
from _serviceprovider_panel.offer.models import Offer

import logging
logger = logging.getLogger('accounts')

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

subtype_list_url=serializers.HyperlinkedIdentityField(view_name='up_garage:up_subcategory',lookup_field='pk')
garage_list_url=serializers.HyperlinkedIdentityField(view_name='up_garage:up_garage',lookup_field='pk')
garage_detail_url=serializers.HyperlinkedIdentityField(view_name='up_garage:up_garage_detail',lookup_field='pk')
submit_review_url=serializers.HyperlinkedIdentityField(view_name='up_garage:up_review',lookup_field='pk')
offer_detail_url=serializers.HyperlinkedIdentityField(view_name='up_garage:up_offer_detail',lookup_field='pk')
make_fav_garage_url=serializers.HyperlinkedIdentityField(view_name='up_accounts:user_fav_gar',lookup_field='pk')
remove_fav_garage_url=serializers.HyperlinkedIdentityField(view_name='up_accounts:user_remove_fav_gar',lookup_field='pk')

class APIException400(APIException):
    status_code=400

class ServiceTypeListSerializer(serializers.ModelSerializer):
    subtype_list_url=subtype_list_url
    id=serializers.CharField()
    class Meta:
        model=ServiceType
        fields=('id','type','icon','subtype_list_url')
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['icon']:
            data['icon'] = ""
        return data
class ServiceSubTypeSerializer(serializers.ModelSerializer):
    garage_list_url=garage_list_url
    class Meta:
        model=ServiceSubType
        fields=('id','subtype','icon','garage_list_url')
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['icon']:
            data['icon'] = ""
        return data
class GarageListSerializer(serializers.ModelSerializer):
    garage_detail_url=garage_detail_url
    make_fav_garage_url=make_fav_garage_url
    remove_fav_garage_url=remove_fav_garage_url
    is_favorite=serializers.SerializerMethodField()

    class Meta:
        model=Garage
        fields=('id','name','store_image1','store_image2','store_image3','lat',
        'lon','location','state','city','make_fav_garage_url','remove_fav_garage_url','is_favorite','garage_rating','garage_detail_url')

    def get_is_favorite(self,instance):
        user=self.context['request'].user.ruser
        if FavoriteGarage.objects.filter(garage=instance,user=user):
            return 'True'
        else:
            return 'False'
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['store_image1']:
            data['store_image1'] = ""
        if not data['store_image2']:
            data['store_image2'] = ""
        if not data['store_image3']:
            data['store_image3'] = ""
        return data

'''
GARAGE DETAIL SERIALIZERS-------
'''
class GarageDetailSerializer(serializers.ModelSerializer):
    is_owner=serializers.CharField(read_only=True)
    make_fav_garage_url=make_fav_garage_url
    remove_fav_garage_url=remove_fav_garage_url
    is_favorite=serializers.SerializerMethodField()
    class Meta:
        model=Garage
        fields=('id','is_owner','name','store_image1','store_image2','store_image3','contact_person',
        'garage_rating','lat','lon','location','state','city','country_code','contact_num',
        'tax_registration_num','tax_registration_date','make_fav_garage_url','remove_fav_garage_url','is_favorite')
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['store_image1']:
            data['store_image1'] = ""
        if not data['store_image2']:
            data['store_image2'] = ""
        if not data['store_image3']:
            data['store_image3'] = ""
        if not data['tax_registration_num']:
            data['tax_registration_num'] = ""
        if not data['tax_registration_date']:
            data['tax_registration_date'] = ""
        return data
    def get_is_favorite(self,instance):
        user=self.context['request'].user.ruser
        if FavoriteGarage.objects.filter(garage=instance,user=user):
            return 'True'
        else:
            return 'False'
class GarageWorkHourSerializer(serializers.ModelSerializer):
    class Meta:
        model=WeeklySchedule
        fields=('day','start_time','end_time')
class GarageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceType
        fields=('type','icon')
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['icon']:
            data['icon'] = ""
        return data
class GarageSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceSubType
        fields=('subtype','icon')
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['icon']:
            data['icon'] = ""
        return data
class GarageOfferSerializer(serializers.ModelSerializer):
    offer_detail_url=offer_detail_url
    class Meta:
        model=Offer
        fields=('id','title','offer_detail_url')
class GarageOfferDetailSerializer(serializers.ModelSerializer):
    garage=serializers.SerializerMethodField()
    class Meta:
        model=Offer
        fields=('garage','title','description','coupon','end_date')
    def get_garage(self,instance):
        return self.context['garage']
class GarageReviewSerializer(serializers.ModelSerializer):
    garage=serializers.CharField(read_only=True)
    # user=serializers.CharField(read_only=True)
    user=serializers.SerializerMethodField()
    profile_image=serializers.SerializerMethodField()
    class Meta:
        model=UserReview
        fields=('garage','user','profile_image','review','rating','created_on')
    def get_user(self,instance):
        if instance.user.last_name:
            return instance.user.first_name+' '+instance.user.last_name
        return instance.user.first_name
    def get_profile_image(self,instance):
        if instance.user.profile_image:
            return instance.user.profile_image.url
        return ''
class GarageAllDetailSerializer(serializers.ModelSerializer):
    submit_review_url=submit_review_url
    # owner_profile=serializers.SerializerMethodField()
    garage_detail=serializers.SerializerMethodField()
    category_detail=serializers.SerializerMethodField()
    subcategory_detail=serializers.SerializerMethodField()
    schedule_detail=serializers.SerializerMethodField()
    offer_detail=serializers.SerializerMethodField()
    review_detail=serializers.SerializerMethodField()
    total_number_of_reviews=serializers.SerializerMethodField()
    class Meta:
        model=Garage
        fields=('garage_detail','schedule_detail','category_detail','subcategory_detail',
        'offer_detail','review_detail','submit_review_url','total_number_of_reviews')

    def get_garage_detail(self,garage):
        if garage is not None:
            instance=garage
            request=self.context['request']
            data=GarageDetailSerializer(instance,context={'request':request}).data
            if data['is_favorite']:
                data['make_fav_garage_url']=''
            else:
                data['remove_fav_garage_url']=''
            return data
    def get_schedule_detail(self,garage):
        if garage is not None:
            queryset=WeeklySchedule.objects.filter(garage=garage)
            data=GarageWorkHourSerializer(queryset,many=True).data
            return data
    def get_category_detail(self,garage):
        if garage is not None:
            instance=garage.service_type
            data=GarageCategorySerializer(instance,many=True).data
            return data
    def get_subcategory_detail(self,garage):
        if garage is not None:
            instance=garage.service_subtype
            data=GarageSubCategorySerializer(instance,many=True).data
            return data
    def get_offer_detail(self,garage):
        if garage is not None:
            request=self.context['request']
            queryset=Offer.objects.filter(garage=garage,end_date__gte=datetime.now())
            data=GarageOfferSerializer(queryset,many=True,context={'request':request}).data
            return data
    def get_review_detail(self,garage):
        if garage is not None:
            queryset=UserReview.objects.filter(garage=garage)
            data=GarageReviewSerializer(queryset,many=True).data
            return data
    def get_total_number_of_reviews(self,garage):
        if garage is not None:
            return UserReview.objects.filter(garage=garage).count()

'''
GIVE REVIEW----------
'''
class UserReviewSerializer(serializers.ModelSerializer):
    garage_id=serializers.CharField(read_only=True,)
    rating=serializers.CharField(allow_blank=True,)
    review=serializers.CharField(allow_blank=True,)
    class Meta:
        model=UserReview
        fields=('garage_id','rating','review',)

    def validate(self,data):
        review=data['review']
        rating=data['rating']

        if not rating or rating=="":
            raise APIException400({
                'message':'rating is required',
                'success':'False'
            })
        if not review or review=="":
            raise APIException400({
                'message':'review is required',
                'success':'False'
            })

        return data

    def create(self, validated_data):
        garage_id=self.context['id']
        rating=validated_data['rating']
        review=validated_data['review']
        ruser=self.context['request'].user.ruser

        garage=Garage.objects.filter(id=garage_id).first()

        if '.' in rating:
            rating=rating.split('.')[0]

        review=UserReview(
            garage=garage,
            user=ruser,
            rating=int(rating),
            review=review,
        )

        review.save()
        a=UserReview.objects.filter(garage=garage).aggregate(Sum('rating'))
        b=UserReview.objects.filter(garage=garage).count()
        garage.garage_rating=a['rating__sum']/b
        garage.save()

        cm=CategoryManager.objects.filter(garage=garage).values('category')
        st=ServiceType.objects.filter(id__in=cm)
        scm=SubCategoryManager.objects.filter(garage=garage).values('subcategory')
        sst=ServiceSubType.objects.filter(id__in=scm)
        for s in st:
            s.category_rating=(s.category_rating+1)/2
            s.save()
        # for ss in sst:
        #     ss.subcategory_rating=(ss.subcategory_rating+1)/2
        #     ss.save()

        return validated_data
