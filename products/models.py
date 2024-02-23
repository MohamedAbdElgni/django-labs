from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to="categories/images", null=True, blank=True)

    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()

    @classmethod
    def get_category_by_id(cls, id):
        return cls.objects.get(id=id)

    @classmethod
    def get_category_by_name(cls, name):
        return cls.objects.get(name=name)

    @classmethod
    def add_category(cls, name):
        return cls.objects.create(name=name)

    def get_img(self):
        # print("*" * 50)
        # print(f"/media/{self.img}")
        return f"/media/{self.img}"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100)
    img = models.ImageField(upload_to="products/images", null=True, blank=True)

    @classmethod
    def get_all_products(cls):
        return cls.objects.all()

    @classmethod
    def get_product_by_id(cls, id):
        return cls.objects.get(id=id)

    @classmethod
    def get_product_by_name(cls, name):
        return cls.objects.get(name=name)

    @classmethod
    def get_product_by_category(cls, category):
        return cls.objects.filter(category=category)

    @classmethod
    def add_product(cls, name, price, category, img):
        return cls.objects.create(name=name, price=price, category=category, img=img)

    def get_img(self):
        return f"/media/{self.img}"
