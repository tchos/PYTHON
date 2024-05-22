from django.urls import path
from fact_app import views

app_name = 'fact_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home_fact"),
]