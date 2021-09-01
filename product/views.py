from django.shortcuts import render
from firestore_db import data_base


product_db = data_base("products")


def form(request, product=None):
    
    if product is None:
        product = {}
    
    categories = get_categories()
    
    return render(request, "product_form.html", {"product":product, "categories":categories})


def delete(request, id):
    
    product_db.document(id).delete()
    return list_all(request)


def get_by_id(request, id):
    
    product = product_db.document(id).get().to_dict()
    product["id"] = id
    
    return form(request, product)


def list_card(request, category=None):

     if category is not None:
          collection = product_db.where("category", "==" , category).get()
          #collection = query.order_by("name").stream()
     else:
          collection = product_db.order_by("name").get()

     products = []

     for doc in collection:
          product = doc.to_dict()
          products.append(product)
     
     categories = get_categories()

     return render(request, "product_card.html", {
          "products" : products, 
          "categories" : categories, 
          "category" : category})


def list_all(request):
     
     collection = product_db.order_by("name").get()
     products = []

     for doc in collection:
          product = doc.to_dict()
          product["id"] = doc.id
          products.append(product)
     
     return render(request, "product_list.html", {"products":products})


def save(request):     
     
     product = { 
               "name" : request.POST.get("name"),
               "price" : request.POST.get("price"),
               "image" : request.POST.get("image"),
               "category" : request.POST.get("category"),
               "decription" : request.POST.get("decription")
     }

     if request.POST.get("id") == "":
          product_db.add(product)
     elif request.POST.get("id") != "":
          product_db.document(request.POST.get("id")).update(product)
          
     product = {}
     return list_all(request)


def get_categories():
     
     collection = data_base("categories").order_by("name").get()
     categories = []
    
     for doc in collection:
         category = doc.to_dict()
         category["id"] = doc.id
         categories.append(category)
     
     return categories
