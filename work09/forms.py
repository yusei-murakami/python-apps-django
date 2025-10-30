from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    due_date = forms.DateField(
        label='期限日',
        required=False,
        widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'})
    )

    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'is_completed']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'タスク名を入力してください'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'is_completed': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }
