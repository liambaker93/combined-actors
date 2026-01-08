from django import forms
from .models import Shows


class ShowsForm(forms.ModelForm):
    """
    A form used by the admin to add new shows to the db
    """
    class Meta:
        model = Shows
        fields = '__all__'
