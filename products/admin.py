from django.contrib import admin

# Register your models here.

from .models import Category, Product

admin.site.register(Category)

admin.site.register(Product)

# then we need to run the following command to create the database table for the models we have created
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# then we can go to the admin page and add some products and categories
