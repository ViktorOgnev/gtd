from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from tinymce.models import HTMLField

from utils.aux_utils import get_image_path, get_file_path, make_hash

from .signal_processors import (create_thumbnail)
from .storage import OverwriteStorage


class Item(models.Model):
    
    IN_BASKET = 1
    IS_PROJECT = 2
    IS_PROJECT_PLAN = 3
    IS_WAITING  = 4
    IN_CALENDAR = 5
    IS_NEXT_ACTION = 6
    IS_TRASH = 7
    IN_SOMEDAY_MAYBE = 8
    IS_REFERENCE = 9
    
    # Options for how to display a post
    
    STATUS_CHOICES = (
        (IN_BASKET, _('In basket')),
        (IS_PROJECT, _('Project')),
        (IS_PROJECT_PLAN, _('Project plan')),
        (IS_WAITING, _('Waiting')),
        (IN_CALENDAR, _('Calendar')),
        (IS_NEXT_ACTION, _('Next action')),
        (IS_TRASH, _('Trash')),
        (IN_SOMEDAY_MAYBE, _('Someday maybe')),
        (IS_REFERENCE, _('Reference')),
    )
    
    
    # Fields representing items content.
    name = models.CharField(max_length=255)
    description = HTMLField(blank=True)
    brief_description = HTMLField(blank=True)
    image = models.ImageField(upload_to=get_image_path, blank=True)
    file = models.ImageField(upload_to=get_file_path, blank=True)
    
    # A reference to project if an instance is one of this project's plans
    # is made available by is_project_plan == True only
    project = models.ForeignKey('self', blank=True, null=True) 
    
    # Categorisation switch
    status = models.IntegerField(choices=STATUS_CHOICES, default=IN_BASKET)
    
    # Helper fields
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
        
    def __unicode__(self):
        return self.name
    
    
    def save(self, force_insert=False, force_update=False):
        if self.date_added:
            self.date_updated = datetime.now()
        else:
            self.date_added = self.date_updated = datetime.now()
        
        if not self.slug:
            self.slug = slugify(make_hash(self.name, str(self.status)))
        
        if not self.brief_description:
            self.brief_description = self.description[0:255]
            
        super(Item, self).save(force_insert, force_update)
    
    def get_absolute_url(self):
        return reverse('core_item_detail', args=(self.slug,))