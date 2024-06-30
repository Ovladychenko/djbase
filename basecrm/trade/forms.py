from datetime import datetime

from django import forms
from setuptools.msvc import winreg

from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class ClientForm(forms.Form):
    guid = forms.CharField(max_length=50, required=False, label="Идентификатор")
    code = forms.CharField(max_length=20, label="Номер", widget=forms.TextInput(
        attrs={'class': 'form-control', 'readonly': 'readonly', 'class': 'form-control-plaintext'}))
    name = forms.CharField(max_length=250, label="Наименование",
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    full_name = forms.CharField(max_length=250, label="Полное наименование",
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    physical_address = forms.CharField(max_length=250, label="Физический адрес",
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    legal_address = forms.CharField(max_length=250, label="Юридический адрес",
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    phones = forms.CharField(max_length=250, label="Телефоны", required=False,
                             widget=forms.Textarea(attrs={'cols': 10, 'rows': 3, 'class': 'form-control'}))
    vat_number = forms.CharField(max_length=20, required=False, label="ИНН",
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 4, 'class': 'form-control'}),
                              required=False, label="Комментарий")


class ReportForm(forms.Form):
    date_start = forms.DateField(widget=DateInput)
    date_end = forms.DateField(widget=DateInput)

    def __init__(self, *args, **kwargs):
        list_param1 = kwargs.pop('listparam1', None)
        super(ReportForm, self).__init__(*args, **kwargs)
        if list_param1:
            self.fields['listparam1'] = forms.CharField(label='Валюта',
                                                        widget=forms.Select(choices=list_param1))


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'cols': 210, 'rows': 23, 'class': 'form-control'})
        }
        labels = {
            'title': 'Заголовок'
        }
