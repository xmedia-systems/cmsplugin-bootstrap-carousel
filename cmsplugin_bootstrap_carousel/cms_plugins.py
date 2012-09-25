# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_bootstrap_carousel.models import *
from django.utils.translation import ugettext as _
from django.contrib import admin

class CarouselItemInline(admin.TabularInline):
    model = CarouselItem

class CarouselPlugin(CMSPluginBase):
    model = Carousel
    name = _("Carousel")
    render_template = "cmsplugin_bootstrap_carousel/carousel.html"

    inlines = [
        CarouselItemInline,
        ]

    def render(self, context, instance, placeholder):
        context.update({'instance' : instance})
        return context

plugin_pool.register_plugin(CarouselPlugin)
