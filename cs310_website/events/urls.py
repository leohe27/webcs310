from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('<int:year>/<str:month>/', views.home, name = 'home'),
    
    path('add_student', views.add_student, name = 'add-student'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('show_student/<student_id>', views.show_student, name = "show-student"),
    path('update_student/<student_id>', views.update_student, name = "update-student"),
    path('search_student', views.search_student, name = 'search-student'),

    path('events', views.all_events, name = 'list-events'),
    path('show_event/<event_id>', views.show_event, name="show-event"),
    path('events/event-one', views.event_one, name="event-one"),
    path('events/event-two', views.event_two, name="event-two"),
    path('events/event-three', views.event_three, name="event-three"),
    path('events/event-four', views.event_four, name="event-four"),
    path('events/event-five', views.event_five, name="event-five"),
    path('events/event-six', views.event_six, name="event-six"),

    path('events/event-complete', views.event_complete, name="event-complete"),
    path('events/lesson-one', views.lesson_one, name = 'lesson-one'),
    path('events/lesson-two', views.lesson_two, name = 'lesson-two'),
    path('events/lesson-three', views.lesson_three, name = 'lesson-three'),
    ]
