from django.urls import path
from .views import index, about, property_list, contact, products_list, product_detail, add_product, product_delete, product_update


urlpatterns = [
  path('', index, name="index"),
  path("add/product/", add_product, name="add_product"),
  path("update/product/<slug:product_slug>/", product_update, name="product_update"),
  path("delete/product/<slug:product_slug>/", product_delete, name="product_delete"),
  path("products/", products_list, name="products-list"),
  path("products/<slug:category_slug>/", products_list, name="products-list-by-cat"),
  path("product/<slug:product_slug>/", product_detail, name="product_detail"),
  path("about/", about, name="about"),
  path("property/list/", property_list, name="property_list"),
  path("contact/", contact, name="contact"),
]
