from rest_framework import generics, filters
from .models import Product, Category, Coupon
from .serializers import ProductSerializer, ProductDetailSerializer, CategorySerializer, CouponSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id', 'name', 'price']

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all().select_related('category')


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CouponListView(generics.ListAPIView):
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()
