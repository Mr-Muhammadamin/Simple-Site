from django.urls import path, re_path
from .views import main_view, about_view, contact_view, product_view, letters_view

urlpatterns = [
    path("", main_view, name="main"),
    re_path(r"^about", about_view, name="about"),
    path("contact/", contact_view, name="contact"),
    # re_path(r'^products/(?P<product_id>\d+)/', product_view),
    path("products/<uuid:product_token>/<slug:slug>/<language>", product_view, name="product-detail"),
    # re_path(r"^letters/[A-Za-z]{3}/[1-9]{2}/$", letters_view)
]

