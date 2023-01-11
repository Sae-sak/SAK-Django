from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectCreateAPIView.as_view()),
    path('<int:pk>/', views.ProjectDetailAPIView.as_view())
]