from django.db import models


class Category(models.Model):
    id = models.BigAutoField(null=False, primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "t_category"


class Coupon(models.Model):
    id = models.BigAutoField(null=False, primary_key=True)
    code = models.CharField(max_length=50, unique=True)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)  # 예: 10.00은 10% 할인

    class Meta:
        db_table = "t_coupon"


class Product(models.Model):
    id = models.BigAutoField(null=False, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()  # 기본 단위는 원
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    discount_rate = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)  # 예: 0.10은 10% 할인
    coupon_applicable = models.BooleanField(default=False)

    class Meta:
        db_table = "t_product"

    def get_discount_price(self):
        if self.discount_rate:
            return self.price - (self.price * float(self.discount_rate))
        return self.price

    def get_final_price(self, coupon_code=None):
        final_price = self.get_discount_price()
        if coupon_code and self.coupon_applicable:
            try:
                coupon_obj = Coupon.objects.get(code=coupon_code)
                print(coupon_obj)
                final_price -= (final_price * float(coupon_obj.discount_rate))
            except Coupon.DoesNotExist:
                print("Coupon not found : {coupon_code}".format(coupon_code=coupon_code))
                pass
        return final_price
