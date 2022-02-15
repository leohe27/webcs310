from django.urls import path
from .import views


urlpatterns = [
    path('login_user', views.login_user, name = 'login'),
    path('logout_user', views.logout_user, name = 'logout'),
    path('register_user', views.register_user, name = 'register_user'),
    # path('<int:year>/<str:month>/', views.home, name = 'home'),
    # path('events', views.all_events, name = 'list-events'),
    ]
