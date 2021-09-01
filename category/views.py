from django.shortcuts import render
from firestore_db import data_base


category_db = data_base("categories")


def form(request, category=None):
    
    if category is None:
        category = {}
    
    return render(request, "category_form.html", {"category":category})


def delete(request, id):
    
    category_db.document(id).delete()
    return list_all(request)


def get_by_id(request, id):
    
    category = category_db.document(id).get().to_dict()
    category["id"] = id
    
    return form(request, category)


def list_all(request):
    
    collection = category_db.order_by("name").get()
    categories = []
    
    for doc in collection:
        category = doc.to_dict()
        category["id"] = doc.id
        categories.append(category)

    return render(request, "category_list.html", {"categories":categories})


def save(request):
    
    category = {
        "name" : request.POST.get("name")
    }
    
    if request.POST.get("id") == "":
        #request.method = "POST"
        category_db.add(category)
    elif request.POST.get("id") != "":
        #request.method = "PUT"
        category_db.document(request.POST.get("id")).update(category)
    
    category = {}
    return list_all(request)