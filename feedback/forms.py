from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['phone_number', 'user_name', 'message', 'contact_method']
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
            'user_name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'message': forms.Textarea(attrs={'placeholder': 'Какой автомобиль Вас интересует?', 'rows': 4}),
            'contact_method': forms.HiddenInput(),  # Скрытое поле
        }