# coding: utf-8
import os
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from filer.fields.image import FilerImageField
from cms.models.pluginmodel import CMSPlugin


DEF_SIZE = (800, 600)
        
class Carousel(CMSPlugin):
    domid = models.CharField(max_length=50, verbose_name=_('Name'))
    interval = models.IntegerField(default=5000)
    
    def __unicode__(self):
        return self.domid

class CarouselItem(models.Model):
    carousel = models.ForeignKey(Carousel)
    caption_title = models.CharField(max_length=100, blank=True, null=True)
    caption_content = models.TextField()
    image = FilerImageField(blank=True, null=True)
