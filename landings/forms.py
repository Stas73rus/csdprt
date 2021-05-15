from django import forms
from django.core.validators import RegexValidator


class NorthValleyContactForm(forms.Form):
    name = forms.CharField(label='ФИО', max_length=100)
    email = forms.EmailField(label="email")
    phone = forms.CharField(label='Номер телефона',
                                   validators=[RegexValidator(
                                       regex=r'^\+?1?\d{9,15}$',
                                        message="Формат номера телефона: '+79999999999'. До 15 символов.")],
                                   max_length=17)