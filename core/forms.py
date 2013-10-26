from django import forms
from django.utils.translation import ugettext_lazy as _



from .models import Item


class ItemForm(forms.ModelForm):

    """
    ModelForm class to create Item instance.
    """
    
    
    
    status = forms.IntegerField(widget=forms.RadioSelect(choices=Item.STATUS_CHOICES))
    
    class Meta:
        model = Item
        fields = ['name', 'description', 'image', 'file', 'project', 'status']
    
        
    