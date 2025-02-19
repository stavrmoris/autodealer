from django import forms
from .models import Brand, Rating, Car

class CarFilterForm(forms.Form):
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), required=False, empty_label="Выберите марку")
    model = forms.ChoiceField(required=False, choices=[], widget=forms.Select(attrs={'disabled': 'disabled'}))
    year_min = forms.IntegerField(required=False, label="Год от")
    year_max = forms.IntegerField(required=False, label="Год до")
    price_min = forms.DecimalField(required=False, label="Цена от")
    price_max = forms.DecimalField(required=False, label="Цена до")
    engine_cc_min = forms.IntegerField(required=False, label="Объем двигателя от")
    engine_cc_max = forms.IntegerField(required=False, label="Объем двигателя до")
    rating = forms.ModelChoiceField(queryset=Rating.objects.all(), required=False, empty_label="Выберите оценку")