from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryListView, CouponListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('coupons/', CouponListView.as_view(), name='coupon-list'),
]