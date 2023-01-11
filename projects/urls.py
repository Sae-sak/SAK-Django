from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list),
    path('<int:id>/', views.project_detail)
]