from django.urls import path
from .views import Auth
urlpatterns = [
    path('', Auth.as_view(), name='Auth'),
    ]