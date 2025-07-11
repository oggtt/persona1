from django.urls import path
from .views import question
urlpatterns = [
    path('', question.as_view(), name='question'),
    ]