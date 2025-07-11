from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('question', include('question.urls')),
    path('User', include('signup.urls')),
    path('Auth', include('login.urls')),
]
