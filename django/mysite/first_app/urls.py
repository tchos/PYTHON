from django.urls import path
from . import views

urlpatterns = [
    path('<int:num1>/<int:num2>/', views.add_view, name="add"),
]