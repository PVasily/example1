from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from django.views.generic.detail import DetailView

from .serializers import (BlogCategorySerialiser,
                          BlogPostSerialiser,
                          BlogPostListRetrieveSerializer,
                          BlogCategorySerialiser,
                          BlogCategoryDetailSerialiser,
                          ProdCategorySerializer,
                          NotebookListRetrieveSerializer,
    #   SmartphoneListRetrieveSerializer,
                          ProdCategoryListRetrieveSerializer,
                          NotebookSerializer, SmartphoneListRetrieveSerializer, SmartphoneSerializer,
                          CustomerSerializer, CartSerializer,
    # SmartphoneSerializer
                          )
from ..mixins import CartMixin
from ..models import (BlogCategory,
                      BlogPost,
                      Customer,
                      Notebook,
    # Smartphone,
                      ProdCategories, Smartphone, CartProduct, Cart
                      )
from ..utils import recalc_cart


class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerialiser
    action_to_serializer = {
        'retrieve': BlogCategoryDetailSerialiser
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerialiser

    action_to_serializer = {
        'list': BlogPostListRetrieveSerializer,
        'retrieve': BlogPostListRetrieveSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


# ############### Cart #######################

class BaseView(viewsets.ModelViewSet):

    def get(self, request, *args, **kwargs):
        categories = ProdCategories.objects.get_categories_for_left_sidebar()
        return render(request, 'index.html', {'categories': categories})


class ProdCategoryViewSet(viewsets.ModelViewSet):
    # queryset = ProdCategories.objects.all()
    queryset = ProdCategories.objects.get_categories_for_left_sidebar()
    serializer_class = ProdCategorySerializer

    action_to_serializer = {
        'list': ProdCategoryListRetrieveSerializer,
        'retrieve': ProdCategoryListRetrieveSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )
    # print(queryset)


class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer

    action_to_serializer = {
        'list': NotebookListRetrieveSerializer,
        'retrieve': NotebookListRetrieveSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class SmartphoneViewSet(viewsets.ModelViewSet):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer

    action_to_serializer = {
        'list': SmartphoneListRetrieveSerializer,
        'retrieve': SmartphoneListRetrieveSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    action_to_serializer = {
        'action': CustomerSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )
#
#
class CartViewSet(CartMixin, viewsets.ModelViewSet):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    action_to_serializer = {
        'action': CartSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )
  
    def get(self, request, *args, **kwargs):
        categories = ProdCategories.objects.get_categories_for_left_sidebar()
        context = {
            'cart': self.cart,
            'categories': categories
        }
        return render(request, 'index.html', context)
#
#
class AddToCartView(CartMixin, viewsets.ModelViewSet, View):

    def get(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.get('ct_model'), kwargs.get('slug')
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        # customer = Customer.objects.get(user=request.user)
        # cart = Cart.objects.get(owner=customer, in_order=False)
        cart_product, created = CartProduct.objects.get_or_create(
            user=self.cart.owner, cart=self.cart, content_type=content_type, object_id=product.id
        )
        if created:
            self.cart.products.add(cart_product)
        # self.cart.save()
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, 'Товар добавлен')
        return HttpResponseRedirect('/cart/')
