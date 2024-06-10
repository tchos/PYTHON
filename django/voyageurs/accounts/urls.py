from django.urls import path
from .views import TeamCreationView, TeamListView, TeamEditView, registerUser, loginView, logoutView, UserListView, UserUpdateView

app_name = "accounts"

urlpatterns = [
    path('team/add/', TeamCreationView.as_view(), name="add_team"),
    path('team/list/', TeamListView.as_view(), name="list_teams"),
    path('team/<int:pk>/edit/', TeamEditView.as_view(), name="edit_team"),
    path('signup/', registerUser, name="signup"),
    path('signin/', loginView, name="signin"),
    path('signout/', logoutView, name="signout"),
    path('list/', UserListView.as_view(), name="list"),
    path('<int:pk>/edit/', UserUpdateView.as_view(), name="edit_user"),
]

# path('edit/<int:pk>/', EditMotView.as_view(), name="edit"),