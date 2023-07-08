from pyexpat import model
from django.forms import ModelForm
from .models import Picture

class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = [
            'name',
            'uploader',
            'image',
        ]