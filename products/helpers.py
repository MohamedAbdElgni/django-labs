import requests


baseurl = "https://fakestoreapi.com/products/"


def get_cats():
    url = baseurl + "categories"
    response = requests.get(url)
    cats = response.json()
    return cats



