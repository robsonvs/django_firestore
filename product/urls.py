from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_card),
    path('list/', views.list_all),
    path('form/', views.form),
    path('save/', views.save),
    path('delete/<str:id>/', views.delete),
    path('<str:category>/', views.list_card),
    path('id/<str:id>/', views.get_by_id),
]