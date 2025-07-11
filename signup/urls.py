from django.urls import path
from .views import User
from login.views import Auth
urlpatterns = [
    path('', User.as_view(), name='User'),
    path('Auth', Auth.as_view(), name='Auth'),

    ]