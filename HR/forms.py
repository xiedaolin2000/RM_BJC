from django.forms import ModelForm
from HR.models import Person

class personForm(ModelForm):
    class Meta:
        model = Person
        fields=["userName","workNo"]
    