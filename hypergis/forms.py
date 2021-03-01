from django import forms
from . models import FarmerFields


class RegisterFarmForm(forms.ModelForm):
    class Meta:
        model = FarmerFields
        fields = ['field_name', 'grass_type', 'grass_age', 'zip_code']
