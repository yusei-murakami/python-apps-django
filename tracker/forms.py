# from django import forms
# from .models import FoodEntry
# from django.forms import ModelForm
# from .models import Entry

# class FoodEntryForm(forms.ModelForm):
#     class Meta:
#         model = FoodEntry
#         fields = ['grams']
        
# class MeasurementForm(forms.ModelForm):
#     class Meta:
#         fields = ['date','temperature','weight','bp_sys','bp_dia','sleep_hours','burned_calories','steps']
#         widgets = {
#             'date': forms.DateInput(attrs={'type':'date'}),
#         }


from django import forms
from .models import FoodEntry, Measurement
from django.forms import ModelForm
from .models import Entry 

class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ['grams']
        
class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement 
        fields = ['date','temperature','weight','bp_sys','bp_dia','sleep_hours','burned_calories','steps']
        
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
        }


# class MeasurementForm(forms.ModelForm):
#     class Meta:
#         model = Measurement 
        
#         fields = [
#             'date',
#             'temperature',
#             'weight',
#             'bp_sys',      
#             'bp_dia',      
#             'sleep_hours',
#             'burned_calories', # calorie_burned を burned_calories に変更
#             'steps'
#         ]
        
#         widgets = {
#             'date': forms.DateInput(attrs={'type':'date'}),
#         }