from product.views import list_all
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.list_all),
    path('form/', views.form),
    path('save/', views.save),
    path('delete/<str:id>/', views.delete),
    path('<str:id>/', views.get_by_id),
]