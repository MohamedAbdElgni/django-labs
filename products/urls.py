from django.urls import path
from .views import *

urlpatterns = [
    path("", Products, name="Products"),
    path("categories/", Categories, name="Categories"),
    path("catupdate/<int:id>/", UpdateCategory, name="UpdateCategory"),
    path("catdelete/<int:id>/", DeleteCategory, name="DeleteCategory"),
    path("catadd/", AddCategory, name="AddCategory"),
    path("cat/<int:id>/", ShowCategory, name="ShowCategory"),
    path("products/", Products, name="Products"),
    path("addprouduct/", AddProduct, name="AddProduct"),
    path("prouduct/<int:id>/", ShowProduct, name="ShowProduct"),
    path("updateprouduct/<int:id>/", UpdateProduct, name="UpdateProduct"),
    path("deleteprouduct/<int:id>/", DeleteProduct, name="DeleteProduct"),
]
