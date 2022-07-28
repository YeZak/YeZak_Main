from django import forms
from .models import Item

class UploadForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'item_name',
            'price',
            'item_size_width',
            'item_size_height',
            'details',
            'item_id',
        ]