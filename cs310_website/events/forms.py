from django import forms
from django.forms import ModelForm
from .models import MyClassStudent
from .models import Classroom


class StudentForm(ModelForm):
	class Meta:
		model = MyClassStudent
		fields = ('name','classroom','badge','teacher')
		labels = {
			'name': '学生名称',
			'classroom':'班级',
			'badge':'奖章',
			'teacher':'老师',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'classroom':forms.TextInput(attrs={'class':'form-control'}),
			'badge':forms.TextInput(attrs={'class':'form-control'}),
			'teacher':forms.TextInput(attrs={'class':'form-control'}),
		}

# class ClassroomForm(ModelForm):
# 	class Meta:
# 		model = Classroom
# 		fields = ('name','classroom','badge')
# 		labels = {
# 			'name': '学生名称',
# 			'classroom':'班级',
# 			'badge':'奖章',
# 		}
# 		widgets = {
# 			'name': forms.TextInput(attrs={'class':'form-control'}),
# 			'classroom':forms.TextInput(attrs={'class':'form-control'}),
# 			'badge':forms.TextInput(attrs={'class':'form-control'}),
# 		}		