from .models import Request
from django.forms import ModelForm, TextInput


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ["request"]
        widgets = {
            "request": TextInput(attrs={'class': "form-control", 'placeholder': "Search..."})
        }
