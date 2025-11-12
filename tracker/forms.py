from django import forms
from .models import Entry, Food

class EntryForm(forms.ModelForm):
	date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class Meta:
	model = Entry
	fields = ['date', 'temperature', 'weight', 'systolic', 'diastolic', 'sleep_hours', 'calorie_burned', 'steps']

class FoodForm(forms.ModelForm):
	class Meta:
		model = Food
		fields = ['name', 'kcal_per_100g']