from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='ShopName'),
    path("about/", views.about, name='AboutUs'),
    path("contact/", views.contact, name='ContactUs'),
    path("tracker/", views.tracker, name='TrackingStatus'),
    path("search/", views.search, name='ShopName'),
    path("products/<int:myid>", views.productView, name='productview'),
    path("checkout/", views.checkout, name='Checkout'),

]
