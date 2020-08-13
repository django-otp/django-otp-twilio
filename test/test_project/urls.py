from django.contrib import admin
import django.contrib.auth.views
from django.urls import path


urlpatterns = [
    path('login/', django.contrib.auth.views.LoginView.as_view()),
    path('logout/', django.contrib.auth.views.LogoutView.as_view()),
    path('admin/', admin.site.urls),
]
