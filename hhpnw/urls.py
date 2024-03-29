"""hhpnw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from hhpnwapi.views import MenuView, OrderView, OrderTypeView, FoodTypeView, PaymentTypeView, OrderItemView, check_user, register_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'menus', MenuView, 'menu')
router.register(r'orders', OrderView, 'order')
router.register(r'ordertypes', OrderTypeView, 'ordertype')
router.register(r'foodtypes', FoodTypeView, 'foodtype')
router.register(r'paymenttypes', PaymentTypeView, 'paymenttype')
router.register(r'orderitems', OrderItemView, 'orderitem')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
