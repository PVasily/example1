from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .mixins import CartMixin
from .models import ProdCategories, CartProduct
from .utils import recalc_cart


def index(request):
    return render(request, 'index.html', {})


def category_detail(request, id):
    return render(request, 'index.html', {})


def post_detail(request, id):
    prinnt(id)
    return render(request, 'index.html', {})


def news(request):
    return render(request, 'index.html', {})


def home(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'index.html', {})

def cart(request):
    return render(request, 'index.html', {})


def product_categories(request):
    context = ProdCategories.objects.get_categories_for_left_sidebar()
    print(context)
    return render(request, 'index.html', {'context': context})


def notebooks(request):
    return render(request, 'index.html', {})


def smartphones(request):
    return render(request, 'index.html', {})




def note_detail(request, id):
    return render(request, 'index.html', {})


def smart_detail(request, id):
    return render(request, 'index.html', {})
