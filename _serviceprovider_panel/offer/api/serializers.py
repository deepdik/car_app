from rest_framework import serializers
from rest_framework.exceptions import APIException

from _serviceprovider_panel.offer.models import *

offer_detail_url=serializers.HyperlinkedIdentityField(view_name='spp_offer:spp_offer_detail',lookup_field='pk')
offer_update_url=serializers.HyperlinkedIdentityField(view_name='spp_offer:spp_offer_update',lookup_field='pk')
offer_delete_url=serializers.HyperlinkedIdentityField(view_name='spp_offer:spp_offer_delete',lookup_field='pk')

class APIException400(APIException):
    satus_code=400

class CreateOfferSerializer(serializers.Serializer):
    garage=serializers.CharField(read_only=True)
    image1=serializers.ImageField(required=False,)
    image2=serializers.ImageField(required=False,)
    image3=serializers.ImageField(required=False,)
    image4=serializers.ImageField(required=False,)
    video1=serializers.FileField(required=False,)
    video2=serializers.FileField(required=False,)
    title=serializers.CharField(allow_blank=True,)
    description=serializers.CharField(allow_blank=True,)
    coupon=serializers.CharField(allow_blank=True,)
    start_date=serializers.CharField(allow_blank=True,)
    end_date=serializers.CharField(allow_blank=True,)

    class Meta:
        model=Offer
        fields=('garage','image1','image2','image3','image4','video1','video2',
        'title','description','coupon','start_date','end_date')

    def validate(self,data):
        title=data['title']
        description=data['description']
        coupon=data['coupon']
        start_date=data['start_date']
        end_date=data['end_date']

        if not title or title=='':
            raise APIException400({
                'messgae':'title can not be blank',
                'success':'False',
            })
        if not description or description=='':
            raise APIException400({
                'messgae':'description can not be blank',
                'success':'False',
            })
        if not coupon or coupon=='':
            raise APIException400({
                'messgae':'coupon can not be blank',
                'success':'False',
            })
        if not start_date or start_date=='':
            raise APIException400({
                'messgae':'start_date can not be blank',
                'success':'False',
            })
        if not end_date or end_date=='':
            raise APIException400({
                'messgae':'end_date can not be blank',
                'success':'False',
            })

        return data

    def create(self,validated_data,*args,**kwargs):
        request=self.context['request']
        garage=self.context['garage']

        image1=request.FILES.get('image1')
        image2=request.FILES.get('image2')
        image3=request.FILES.get('image3')
        image4=request.FILES.get('image4')
        video1=request.FILES.get('video1')
        video2=request.FILES.get('video2')
        title=validated_data['title']
        description=validated_data['description']
        coupon=validated_data['coupon']
        start_date=validated_data['start_date']
        end_date=validated_data['end_date']

        offer=Offer(
            garage=garage,
            image1=image1,
            image2=image2,
            image3=image3,
            image4=image4,
            video1=video1,
            video2=video2,
            title=title,
            description=description,
            coupon=coupon,
            start_date=start_date,
            end_date=end_date,
        )
        offer.save()

        validated_data['garage']=garage
        validated_data['image1']=offer.image1
        validated_data['image2']=offer.image2
        validated_data['image3']=offer.image3
        validated_data['image4']=offer.image4
        validated_data['video1']=offer.video1
        validated_data['video2']=offer.video2

        return validated_data

class GarageWiseOfferListSerializer(serializers.ModelSerializer):
    offer_detail_url=offer_detail_url
    class Meta:
        model=Offer
        fields=('offer_detail_url','garage','image1','image2','image3','image4','video1','video2',
        'title','description','coupon','start_date','end_date')
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['image1']:
            data['image1'] = ""
        if not data['image2']:
            data['image2'] = ""
        if not data['image3']:
            data['image3'] = ""
        if not data['image4']:
            data['image4'] = ""
        if not data['video1']:
            data['video1'] = ""
        if not data['video2']:
            data['video2'] = ""
        return data

class OfferDetailSerializer(serializers.ModelSerializer):
    offer_update_url=offer_update_url
    offer_delete_url=offer_delete_url
    class Meta:
        model=Offer
        fields=('offer_update_url','offer_delete_url','garage','image1','image2','image3','image4','video1','video2',
        'title','description','coupon','start_date','end_date')
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['image1']:
            data['image1'] = ""
        if not data['image2']:
            data['image2'] = ""
        if not data['image3']:
            data['image3'] = ""
        if not data['image4']:
            data['image4'] = ""
        if not data['video1']:
            data['video1'] = ""
        if not data['video2']:
            data['video2'] = ""
        return data

class OfferUpdateSerializer(serializers.ModelSerializer):
    garage=serializers.CharField(read_only=True)
    image1=serializers.ImageField(required=False,)
    image2=serializers.ImageField(required=False,)
    image3=serializers.ImageField(required=False,)
    image4=serializers.ImageField(required=False,)
    video1=serializers.FileField(required=False,)
    video2=serializers.FileField(required=False,)
    title=serializers.CharField(allow_blank=True,)
    description=serializers.CharField(allow_blank=True,)
    coupon=serializers.CharField(allow_blank=True,)
    start_date=serializers.CharField(allow_blank=True,)
    end_date=serializers.CharField(allow_blank=True,)

    class Meta:
        model=Offer
        fields=('garage','image1','image2','image3','image4','video1','video2',
        'title','description','coupon','start_date','end_date')

    def validate(self,data):
        title=data['title']
        description=data['description']
        coupon=data['coupon']
        start_date=data['start_date']
        end_date=data['end_date']

        if not title or title=='':
            raise APIException400({
                'messgae':'title can not be blank',
                'success':'False',
            })
        if not description or description=='':
            raise APIException400({
                'messgae':'description can not be blank',
                'success':'False',
            })
        if not coupon or coupon=='':
            raise APIException400({
                'messgae':'coupon can not be blank',
                'success':'False',
            })
        if not start_date or start_date=='':
            raise APIException400({
                'messgae':'start_date can not be blank',
                'success':'False',
            })
        if not end_date or end_date=='':
            raise APIException400({
                'messgae':'end_date can not be blank',
                'success':'False',
            })

        return data

    def create(self,validated_data,*args,**kwargs):
        request=self.context['request']
        offer=self.context['offer']

        image1=request.FILES.get('image1')
        image2=request.FILES.get('image2')
        image3=request.FILES.get('image3')
        image4=request.FILES.get('image4')
        video1=request.FILES.get('video1')
        video2=request.FILES.get('video2')
        title=validated_data['title']
        description=validated_data['description']
        coupon=validated_data['coupon']
        start_date=validated_data['start_date']
        end_date=validated_data['end_date']

        offer.image1=image1
        offer.image2=image2
        offer.image3=image3
        offer.image4=image4
        offer.video1=video1
        offer.video2=video2
        offer.title=title
        offer.description=description
        offer.coupon=coupon
        offer.start_date=start_date
        offer.end_date=end_date

        offer.save()

        validated_data['garage']=offer.garage
        validated_data['image1']=offer.image1
        validated_data['image2']=offer.image2
        validated_data['image3']=offer.image3
        validated_data['image4']=offer.image4
        validated_data['video1']=offer.video1
        validated_data['video2']=offer.video2

        return validated_data

class SubPlanListSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubscriptionPlan
        fields=('plan_name','plan_desc','price','validity_from','validity_to','created_on')
