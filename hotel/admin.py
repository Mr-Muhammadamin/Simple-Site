from django.contrib import admin
from .models import Category, Product, ProductImage, Discount, Comment

admin.site.register(Comment)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ("title", "slug")
  search_fields = ("title", "slug")
  prepopulated_fields = {"slug": ("title", )}


class ProductImageAdmin(admin.StackedInline):
  model = ProductImage
  extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ("title", "slug", "price", "quantity", "stock_status")
  # list_display_links = ("title", "price")
  prepopulated_fields = {"slug": ("title", )}
  fields = ("id", "title", "slug", "description", "price", "quantity", "stock_status", "category", "discount", "author", "created", "updated")
  readonly_fields = ("id", "author", "created", "updated")
  list_filter = ("created", "updated", "stock_status", "category")
  inlines = [ProductImageAdmin]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
  list_display = ("name", "percent", "deadline")
