from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Category, Product

# Create your views here.


def Categories(request):
    categories = Category.get_all_categories()
    return render(request, "categories/categories.html", {"categories": categories})


def UpdateCategory(request, id):
    if request.method == "POST":
        # print(request.POST)
        # print(request.FILES)
        category = Category.objects.get(id=id)

        if "img" in request.FILES:

            category.name = request.POST["name"]
            category.description = request.POST["description"]
            category.img = request.FILES["img"]
            category.save()
        else:
            category.name = request.POST["name"]
            category.description = request.POST["description"]
            category.save()

        return HttpResponseRedirect(reverse("Categories"))
    else:
        category = Category.get_category_by_id(id)
        return render(request, "categories/update_cat.html", {"category": category})


def DeleteCategory(request, id):

    Category.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse("Categories"))


def AddCategory(request):
    if request.method == "POST":
        # print(request.POST)
        # print(request.FILES)
        category = Category()
        category.name = request.POST["name"]
        category.description = request.POST["description"]
        category.img = request.FILES["img"]
        category.save()
        return HttpResponseRedirect(reverse("Categories"))
    else:
        return render(request, "categories/add_cat.html")


def ShowCategory(request, id):
    category = Category.get_category_by_id(id)

    return render(request, "categories/show_cat.html", {"category": category})


def Products(request):
    products = Product.get_all_products()
    return render(request, "products/products.html", {"products": products})


def AddProduct(request):
    if request.method == "POST":
        # print(request.POST)
        # print(request.FILES)
        product = Product()
        product.name = request.POST["name"]
        product.price = request.POST["price"]
        product.category = Category.get_category_by_name(request.POST["category"]).name
        product.img = request.FILES["img"]
        product.save()
        return HttpResponseRedirect(reverse("Products"))
    else:
        categories = Category.get_all_categories()
        return render(request, "products/add_prod.html", {"categories": categories})


def ShowProduct(request, id):
    product = Product.get_product_by_id(id)

    return render(request, "products/show_prod.html", {"product": product})


def UpdateProduct(request, id):
    if request.method == "POST":
        # print(request.POST)
        # print(request.FILES)
        product = Product.objects.get(id=id)

        product.name = request.POST["name"]
        product.price = request.POST["price"]
        product.category = Category.objects.get(id=request.POST["category"]).name
        if "img" in request.FILES:
            product.img = request.FILES["img"]

        product.save()
        

        return HttpResponseRedirect(reverse("Products"))
    else:
        product = Product.get_product_by_id(id)
        categories = Category.get_all_categories()
        print(categories)
        return render(
            request,
            "products/update_product.html",
            {"product": product, "categories": categories},
        )


def DeleteProduct(request, id):

    Product.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse("Products"))
