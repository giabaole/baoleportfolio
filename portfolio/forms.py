from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'contact__input'}),
        } #updates the input class to have the correct Bulma class and placeholder
        # 'class' : 'input', 'placeholder' : 'City Name'