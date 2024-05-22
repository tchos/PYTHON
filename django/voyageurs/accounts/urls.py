from django.urls import path
from .views import TeamCreationView, registerUser, loginView, logoutView, UserListView

app_name = "accounts"

urlpatterns = [
    path('team/add/', TeamCreationView.as_view(), name="add_team"),
    path('signup/', registerUser, name="signup"),
    path('signin/', loginView, name="signin"),
    path('signout/', logoutView, name="signout"),
    path('list/', UserListView.as_view(), name="list"),
]

# path('edit/<int:pk>/', EditMotView.as_view(), name="edit"),