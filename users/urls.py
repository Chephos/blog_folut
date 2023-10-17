from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("register", views.Register.as_view(), name="register"),
    path('user/<str:username>/', views.UserDetailView.as_view(), name='user_detail'),
]
