from django.urls import path
from.views import index, sale, cart, checkout

urlpatterns = [

    path("", index),
    path("sale/", sale),
    path("cart/", cart),
    path("checkout/", checkout)


]