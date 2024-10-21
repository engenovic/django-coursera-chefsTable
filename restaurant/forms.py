from django import forms
from .models import Customer

POSTS = (
    ("1", "Manager"), 
    ("2", "Cashier"),
    ("3", "Operator"),
    )


class ApplicationForm(forms.Form):
    name = forms.CharField(label='Name of Applicant', max_length=50)
    address = forms.CharField(label='Address', max_length=100)
    posts = forms.ChoiceField(choices=POSTS)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
