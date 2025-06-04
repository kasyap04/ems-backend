from django.urls import path
from user_profile.views import UserDetailView

urlpatterns = [
    path("", UserDetailView.as_view(), name="user-detail"),
]