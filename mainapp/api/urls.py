from django.urls import path

from rest_framework import routers

from .views import (
    AddToCartView,
    BlogCategoryViewSet,
    BlogPostViewSet,
    CustomerViewSet,
    ProdCategoryViewSet,
    NotebookViewSet,
    BaseView,
    SmartphoneViewSet,
    CartViewSet,
)

router = routers.SimpleRouter()
router.register('category', BlogCategoryViewSet, basename='category')
router.register('posts', BlogPostViewSet, basename='posts')
router.register('customers', CustomerViewSet, basename='customers')
router.register('prodcategories', ProdCategoryViewSet, basename='prodcategories')
router.register('notebooks', NotebookViewSet, basename='notebooks')
router.register('smartphones', SmartphoneViewSet, basename='smartphones')
router.register('cart', CartViewSet, basename='cart')
router.register('add_to_cart', AddToCartView, basename='add_to_cart')


urlpatterns = [
    # path('test-api/', TestAPIView.as_view(), name='test'),
    # path('thing-api/', ThingAPI.as_view(), name='thing')
]
urlpatterns += router.urls
