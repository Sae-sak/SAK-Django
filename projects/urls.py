from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list),
    path('<int:pk>/', views.ProjectDetailAPIView.as_view())
]