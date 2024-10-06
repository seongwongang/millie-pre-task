from rest_framework import serializers
from millie_pre_task.products.models import Product, Category, Coupon
from millie_pre_task.products import const


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id', 'code', 'discount_rate']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    coupons = CouponSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        data = {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'price': instance.price,
            'category': instance.category.name,
            'coupon_applicable': instance.coupon_applicable,
        }
        if representation['discount_rate'] != const.DISCOUNT_RATE_ZERO:
            data['discount_rate'] = representation['discount_rate']
        return data

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price',
            'category', 'discount_rate',
            'coupon_applicable', 'coupons'
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    discount_price = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price',
            'category', 'discount_rate',
            'coupon_applicable', 'discount_price',
            'final_price',
        ]

    def get_discount_price(self, obj):
        return obj.get_discount_price()

    def get_final_price(self, obj):
        coupon_code = self.context['request'].query_params.get('coupon_code')
        return obj.get_final_price(coupon_code)
