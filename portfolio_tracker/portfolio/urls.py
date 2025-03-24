from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/', include("django.contrib.auth.urls"), name="login"),
    path('account/logout/', views.logout, name='logout'),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
