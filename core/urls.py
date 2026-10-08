from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("products/", views.products, name="products"),
    path("membership/", views.membership, name="membership"),
    path("contact/", views.contact, name="contact"),
    path("news/", views.news, name="news"),
    path("gallery/", views.gallery, name="gallery"),
]
