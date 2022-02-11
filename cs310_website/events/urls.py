from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('<int:year>/<str:month>/', views.home, name = 'home'),
    path('events', views.all_events, name = 'list-events'),
    path('add_student', views.add_student, name = 'add-student'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('show_student/<student_id>', views.show_student, name = "show-student"),
    path('update_student/<student_id>', views.update_student, name = "update-student"),
    path('search_student', views.search_student, name = 'search-student'),
    path('show_event/<event_id>', views.show_event, name="show-event"),
    path('events/event-one', views.event_one, name="event-one"),
    path('events/event-two', views.event_two, name="event-two"),
    ]
