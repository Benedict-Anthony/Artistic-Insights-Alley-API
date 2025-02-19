from django.urls import path
from .views import UserCreateView, UserView
urlpatterns = [
    path('register', UserCreateView.as_view()),
    path('', UserView.as_view()),
]
