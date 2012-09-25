# coding: utf-8
import os
from django.db import models
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from cms.models.pluginmodel import CMSPlugin
from PIL import Image
from cStringIO import StringIO

DEF_SIZE = (800, 600)

class Carousel(CMSPlugin):
    domid = models.CharField(max_length=50)
    interval = models.IntegerField(default=5000)

    def __str__(self):
        return self.domid

class CarouselItem(models.Model):
    carousel = models.ForeignKey(Carousel)
    caption_title = models.CharField(max_length=100)
    caption_content = models.TextField()
    image = models.ImageField(upload_to="uploads/")

    def save(self, *args, **kwargs):
        img = Image.open(self.image.file)
        if img.mode not in ('L', 'RGB'):
            img = img.convert('RGB')
        if hasattr(settings, "BOOTSTRAP_CAROUSEL_IMGSIZE"):
            size = settings.BOOTSTRAP_CAROUSEL_IMGSIZE
        else:
            size = DEF_SIZE
        img.thumbnail(size, Image.ANTIALIAS)

        temp_handle = StringIO()
        img.save(temp_handle, 'png')
        temp_handle.seek(0)

        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                                 temp_handle.read(), content_type='image/png')
        fname = "%s.png" % os.path.splitext(self.image.name)[0]
        self.image.save(fname, suf, save=False)

        super(CarouselItem, self).save()
