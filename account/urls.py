from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('sign-up/', views.signup_page, name='signup'),
]
