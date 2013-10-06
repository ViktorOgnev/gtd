from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

class Item(models.Model):
    # Fields representing items content.
    name = models.CharField()
    description = HTMLField(blank=True)
    brief_description = HTMLField(blank=True)
    image = models.ImageField(upload_to=get_image_path, blank=True)
    file = models.ImageField(upload_to=get_file_path, blank=True)
    
    # A reference to project if an instance is one of this project's plans
    # is made available by is_project_plan == True only
    project = models.ForeignKey(self) 
    
    # Categorisation switches
    in_basket = models.BooleanField(default=False, blank=True)
    is_project = models.BooleanField(default=False, blank=True)
    is_project_plan  = models.BooleanField(default=False, blank=True)
    is_waiting = models.BooleanField(default=False, blank=True)
    in_calendar = models.BooleanField(default=False, blank=True)
    is_next_action = models.BooleanField(default=False, blank=True)
    is_trash = models.BooleanField(default=False, blank=True)
    in_someday_maybe = models.BooleanField(default=False, blank=True)
    is_reference  = models.BooleanField(default=False, blank=True)
    
    # Helper fields
    slug = models.CharField(unique=True)
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
        
    def __unicode__(self):
        return self.name
    
    
        