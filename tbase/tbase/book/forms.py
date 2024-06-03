
#tbase/tbase/book/forms.py
from django.forms import ModelForm, DateTimeInput
from django import forms
from .models import Prebook, Room_Info, Serv_Info

class PrebookForm(ModelForm):
    class Meta:
        model = Prebook
        fields = [ 'room_nums', 'serv_n', 'b_start', 'b_end']

        widgets = {
            'b_start': DateTimeInput(attrs={'placeholder': 'Дата заезда'}),
            'b_end': DateTimeInput(attrs={'placeholder': 'Дата выезда'})
        }



class BookingForm(forms.ModelForm):
    class Meta:
        model = Prebook
        fields = ['b_start', 'b_end','room_nums', 'serv_n']
        labels = {
            'b_start': 'Время заезда',
            'b_end': 'Время выезда',
            'room_nums': 'Выбор дома',
            'serv_n': 'Выбор услуги',
        }
        widgets = {
            'b_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'b_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'room_nums': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'serv_n': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),

        }

