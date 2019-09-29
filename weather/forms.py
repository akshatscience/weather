from django.forms import ModelForm, TextInput
from .models import weather
class weatherForm(ModelForm):
    class meta:
        model = weather
        field = ['name']