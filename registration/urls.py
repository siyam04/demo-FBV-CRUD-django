from django.urls import path
from .views import signup
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', auth_views.login, {'template_name': 'home.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'home.html'}, name='logout'),

]
