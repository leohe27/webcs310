from django.shortcuts import render, redirect
from datetime import datetime 
from .models import Event
from .models import MyClassStudent
from .forms import StudentForm
from django.http import HttpResponseRedirect
from django.db.models import F

def event_complete(request):
	submitted = False
	if request.method == 'POST':
		classname = request.POST['ClassName']
		if classname == 'A':
			MyClassStudent.objects.filter(classroom__name='A').update(badge=F('badge') + 1)
		else:
			MyClassStudent.objects.filter(classroom__name='B').update(badge=F('badge') + 1)
		submitted = True
	else:
		if submitted in request.GET:
			submitted = True
	return render(request,
			'events/event_complete.html',{
			'submitted':submitted
			})	

def event_one(request):
	name = 'Leo'
	return render(request, 
		'events/event_one.html', {
		'name' : name,
		})

def event_two(request):
	name = 'Leo'
	return render(request, 
		'events/event_two.html', {
		'name' : name,
		})

def event_three(request):
	name = 'Leo'
	return render(request, 
		'events/event_three.html', {
		'name' : name,
		})

def event_four(request):
	name = 'Leo'
	return render(request, 
		'events/event_four.html', {
		'name' : name,
		})	

def event_five(request):
	name = 'Leo'
	return render(request, 
		'events/event_five.html', {
		'name' : name,
		})

def event_six(request):
	name = 'Leo'
	return render(request, 
		'events/event_six.html', {
		'name' : name,
		})


def search_student(request):
	if request.method == "POST":
		searched = request.POST['searched']
		students = MyClassStudent.objects.filter(name__contains = searched)
		return render(request,
			'events/search_student.html',
			{'searched':searched,
			'students':students})
	else:
		return render(request,'events/search_student.html',{})

def add_student(request):
	submitted = False
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_student?submitted=True')
	else:
		form = StudentForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'events/add_student.html', {
		'form' : form, 
		'submitted' : submitted
		})

def update_student(request, student_id):
	student = MyClassStudent.objects.get(pk=student_id,)
	form = StudentForm(request.POST or None, instance = student)
	if form.is_valid():
			form.save()
			return redirect('dashboard')

	return render(request,'events/update_student.html',{
		'Student':student,
		'form':form
		})

def show_student(request, student_id):
	student = MyClassStudent.objects.get(pk=student_id,)
	return render(request,
		'events/show_student.html',{
		'Student':student,
		})

def show_event(request, event_id):
	event = Event.objects.get(pk=event_id,)
	return render(request,
		'events/show_event.html',{
		'event':event,
		})

def dashboard(request):
	dashboard = MyClassStudent.objects.all()
	return render(request,
		'events/dashboard.html',{
		'Student':dashboard,
		})

def all_events(request):
	event_list = Event.objects.all()
	return render(request, 
		'events/event_list.html', {
		'event_list' : event_list
		})

def lesson_one(request):
	event_list = Event.objects.all()
	return render(request, 
		'events/lesson_one.html', {
		'event_list' : event_list
		})

def lesson_two(request):
	event_list = Event.objects.all()
	return render(request, 
		'events/lesson_two.html', {
		'event_list' : event_list
		})

def lesson_three(request):
	event_list = Event.objects.all()
	return render(request, 
		'events/lesson_three.html', {
		'event_list' : event_list
		})

def home(request, year = datetime.now().year, month = datetime.now().strftime('%B')):
	name = 'Leo' 
	return render(request, 
		'events/home.html', {
		'name' : name,
		'year' : year,
		'month': month,
		})


