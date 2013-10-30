from django.forms import (CharField, ModelForm, Textarea, TextInput,
                          RadioSelect, ClearableFileInput, Select
                          )
from django.utils.translation import ugettext_lazy as _



from .models import Item


class ItemForm(ModelForm):

    """
    ModelForm class to create Item instance.
    """
    #status = forms.IntegerField(widget=forms.)
    
    
    class Meta:
        model = Item
        fields = ['name', 'description', 'image', 'file', 'project', 'status']
        widgets = {
            'name': TextInput(
                attrs={
                    'type':'text',
                    'class':'form-control'
                }
            ),
            'description': Textarea(
                attrs={
                    'cols': 80,
                    'rows': 5,
                    'class':'form-control'
                },
            ),
            'status': RadioSelect(
                choices=Item.STATUS_CHOICES, 
                attrs={
                    #'class': 'form-control'
                }                  
            ),
            'image': ClearableFileInput(
                attrs={
                    'type': 'file',
                    #'class': 'form-control',
                }
            ),
            'file': ClearableFileInput(
                attrs={
                    'type': 'file',
                    #'class': 'form-control',
                }
            ),
            'project': Select(
                choices=Item.objects.values().filter(status=Item.IS_PROJECT),
                attrs={
                    'class': 'form-control',
                }
            )
        }
        
    