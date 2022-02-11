from django.contrib import admin
from .models import Classroom
from .models import Event
from .models import MyClassStudent

#admin.site.register(Classroom)
#admin.site.register(Event)
admin.site.register(MyClassStudent)

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
	list_display = ('name', 'address')
	ordering = ('name',)
	search_fields = ('name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	fields = (('name'),'description',)
	