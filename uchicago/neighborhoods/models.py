from __future__ import unicode_literals

from django.db import models

# import for the CMS
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, TabbedInterface, ObjectList, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailsearch import index


# Create your models here.
class neighborhoodCHI(models.Model):
	dnaurl = models.CharField(max_length=255, default='', blank=False, null=False)
	name = models.CharField(max_length=255, default='', blank=False, null=False)

	def __unicode__(self):
		return self.name


# models for the CMS below
class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

# model class for map drawing tools
class DrawMapBlock(blocks.StructBlock):
	drawnNeighborhood = models.TextField(default='')

	class Meta:
		template = 'neighborhoods/blocks/map.html'
		icon = 'site'
		label = 'Draw Hood'

class NeighborhoodPage(Page):

    # Database fields
    date = models.DateField("Updated On")
    neighborhood = models.ForeignKey(neighborhoodCHI, on_delete=models.PROTECT)
    draw_neighborhood = StreamField([
    	('draw', DrawMapBlock()),
    ],null=False,blank=False)
    main_content = StreamField([
        ('heading', blocks.CharBlock(classname="heading")),
        ('paragraph', blocks.RichTextBlock()),
        ('link', blocks.URLBlock()),
        ('image', ImageChooserBlock()),
        ('video', EmbedBlock()),
        ('document', DocumentChooserBlock()),
    ])

    # Search index configuraiton
    search_fields = Page.search_fields + [
        index.SearchField('main_content'),
        index.FilterField('date'),
    ]

    # Editor panels configuration
    content_panels = Page.content_panels + [
    	FieldPanel('neighborhood'),
    	StreamFieldPanel('draw_neighborhood'),
    	StreamFieldPanel('main_content'),
    	FieldPanel('date'),
    ]

    edit_handler = TabbedInterface([
    	ObjectList(content_panels, heading='Content'),
    ])

    # Parent page / subpage type rules
    parent_page_types = ['neighborhoods.HomePage']
    subpage_types = []



