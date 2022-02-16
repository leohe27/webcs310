from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):
	name = models.CharField('Classroom Name', max_length=120 )
	address = models.CharField(max_length=300 )
	# attendees = models.ManyToManyField(MyClassStudent, blank=True)
	
	def __str__(self):
		return self.name

class MyClassStudent(models.Model):
	name = models.CharField(max_length=30)
	classroom = models.ForeignKey(Classroom, blank = True, null = True, on_delete=models.CASCADE)
	badge = models.CharField(max_length=30, blank = True, null = True)
	teacher = models.CharField(max_length=60)
	def __str__(self):
		return self.name
		
class Event(models.Model):
	name = models.CharField('Event Name', max_length=120 ) 
	description = models.TextField(blank = True)
	lesson = models.IntegerField("Lesson Number", blank=False)
	reward = models.IntegerField("Badge",blank=False, default="1")
	def __str__(self):
		return self.name


