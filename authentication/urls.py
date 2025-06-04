from django.urls import path
from authentication.views import RegisterView, LoginView, GenerateAccessTokenView, ChangePasswordView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('refresh/', GenerateAccessTokenView.as_view()),
    path('register/', RegisterView.as_view()),
    path('change-password', ChangePasswordView.as_view())
    # path('api/', include('emsapp.urls')),
]
