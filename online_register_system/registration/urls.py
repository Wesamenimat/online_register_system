from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('schedule/', views.schedule, name='schedule'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
