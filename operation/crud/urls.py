from django import views
from django.urls import path
from.import views



urlpatterns = [
    path('', views.index, name="index"),
    path('showdata/', views.showdata, name="showdata"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
]
