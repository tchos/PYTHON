from django.urls import path
from .views import PersonCreateView, PersonUpdateView, PersonListView, StatistiquesView

app_name = 'persons'

urlpatterns = [
    path('new/', PersonCreateView.as_view(), name="add"),
    path('<int:pk>/edit/', PersonUpdateView.as_view(), name="edit"),
    path('list/', PersonListView.as_view(), name="list"),
    path('statistiques/', StatistiquesView.as_view(), name="statistiques"),
]