from .models import Car
from django.forms import ModelForm

class CarForm(ModelForm):
    class Meta:
        model = Car 
        fields = '__all__'
