"""taskmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from mainapp.views import (cart, index,
                           category_detail,
                           post_detail,
                           news,
                           home,
                           login,
                           product_categories,
                           notebooks, note_detail, smart_detail, smartphones,

                           )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mainapp.api.urls')),
    path('category/<int:id>/', category_detail),
    path('posts/<int:id>/', post_detail),
    path('news/', news),
    path('home/', home),
    path('', index),
    path('login/', login),
    path('prodcategories/', product_categories),
    path('notebooks/', notebooks),
    path('smartphones/', smartphones),
    path('notebooks/<int:id>', note_detail),
    path('smartphones/<int:id>', smart_detail),
    path('cart/', cart)
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
