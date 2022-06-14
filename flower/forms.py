from .models import FlowerModel, ModelPosting
from django import forms

class FlowerUpload(forms.ModelForm):
    class Meta:
        model = FlowerModel
        fields = ['image']

class FormUmum(forms.ModelForm):
    class Meta:
        model = ModelPosting
        fields = ['image','posting']

