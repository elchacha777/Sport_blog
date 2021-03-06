from django.urls import path

from account.views import RegistrationView, ActivateView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activation/<str:activation_code>/', ActivateView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]