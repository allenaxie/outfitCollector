from django.forms import ModelForm
from .models import Accessories

class AccessoriesForm(ModelForm):
    class Meta:
        model = Accessories
        exclude = ['outfit']