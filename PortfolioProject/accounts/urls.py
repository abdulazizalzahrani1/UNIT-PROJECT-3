from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.account_view, name="account_view"),
    path('login/', views.login_view, name="login_view"),
    path('register/', views.register_view, name="register_view"),
    path('logout/', views.logout_view, name="logout_view"),
]
