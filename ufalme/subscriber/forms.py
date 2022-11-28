from dataclasses import field
from .models import CustomerInformations
from django.forms import ModelForm

class CustomerInformationsForm(ModelForm):
  class Meta:
    model =CustomerInformations
    fields = '__all__'
    exclude =[
      'created_at',
      'updated_at'
    ]