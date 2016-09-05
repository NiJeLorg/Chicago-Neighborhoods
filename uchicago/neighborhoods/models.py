from __future__ import unicode_literals

from django.db import models

# import for the CMS
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, TabbedInterface, ObjectList, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailsearch import index


# Create your models here.

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

class ChicagoNeighborhoods(Page):

    # Database fields
    date = models.DateField("Updated On")
    introductory_text = models.CharField(max_length=255, default='', null=False, blank=False)
    introductory_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    draw_neighborhood = StreamField([
    	('draw', DrawMapBlock()),
    ],null=False,blank=False)
    social_mix = StreamField([
        ('heading', blocks.CharBlock(classname="heading")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('video', EmbedBlock()),
        ('document', DocumentChooserBlock()),
    ])
    public_space = StreamField([
        ('heading', blocks.CharBlock(classname="heading")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('video', EmbedBlock()),
        ('document', DocumentChooserBlock()),
    ])
    amenities = StreamField([
        ('heading', blocks.CharBlock(classname="heading")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('video', EmbedBlock()),
        ('document', DocumentChooserBlock()),
    ])
    connections = StreamField([
        ('heading', blocks.CharBlock(classname="heading")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('video', EmbedBlock()),
        ('document', DocumentChooserBlock()),
    ])

    # Search index configuraiton
    search_fields = Page.search_fields + [
    	index.SearchField('introductory_text'),
        index.SearchField('social_mix'),
        index.SearchField('public_space'),
        index.SearchField('amenities'),
        index.SearchField('connections'),
        index.FilterField('date'),
    ]

    # Editor panels configuration
    content_panels = Page.content_panels + [
    	FieldPanel('introductory_text'),
    	ImageChooserPanel('introductory_image'),
    	StreamFieldPanel('draw_neighborhood'),
    	StreamFieldPanel('social_mix'),
    	StreamFieldPanel('public_space'),
    	StreamFieldPanel('amenities'),
    	StreamFieldPanel('connections'),
    	FieldPanel('date'),
    ]

    edit_handler = TabbedInterface([
    	ObjectList(content_panels, heading='Content'),
    ])

    # Parent page / subpage type rules
    parent_page_types = ['neighborhoods.HomePage']
    subpage_types = []

class UrbanDesign(Page):

    # Database fields
    date = models.DateField("Updated On")
    introductory_text = models.CharField(max_length=255, default='', null=False, blank=False)
    introductory_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    draw_neighborhood = StreamField([
    	('draw', DrawMapBlock()),
    ],null=False,blank=False)
    sketches = StreamField([
        ('heading', blocks.CharBlock(classname="heading")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('video', EmbedBlock()),
        ('document', DocumentChooserBlock()),
    ])
    city_beautiful = StreamField([
        ('heading', blocks.CharBlock(classname="heading")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('video', EmbedBlock()),
        ('document', DocumentChooserBlock()),
    ])
    transects = StreamField([
        ('heading', blocks.CharBlock(classname="heading")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('video', EmbedBlock()),
        ('document', DocumentChooserBlock()),
    ])
    diversity = StreamField([
        ('heading', blocks.CharBlock(classname="heading")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('video', EmbedBlock()),
        ('document', DocumentChooserBlock()),
    ])
    civic_art = StreamField([
        ('heading', blocks.CharBlock(classname="heading")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('video', EmbedBlock()),
        ('document', DocumentChooserBlock()),
    ])

    # Search index configuraiton
    search_fields = Page.search_fields + [
    	index.SearchField('introductory_text'),
        index.SearchField('sketches'),
        index.SearchField('city_beautiful'),
        index.SearchField('transects'),
        index.SearchField('diversity'),
        index.SearchField('civic_art'),
        index.FilterField('date'),
    ]

    # Editor panels configuration
    content_panels = Page.content_panels + [
    	FieldPanel('introductory_text'),
    	ImageChooserPanel('introductory_image'),
    	StreamFieldPanel('draw_neighborhood'),
    	StreamFieldPanel('sketches'),
    	StreamFieldPanel('city_beautiful'),
    	StreamFieldPanel('transects'),
    	StreamFieldPanel('diversity'),
    	StreamFieldPanel('civic_art'),
    	FieldPanel('date'),
    ]

    edit_handler = TabbedInterface([
    	ObjectList(content_panels, heading='Content'),
    ])

    # Parent page / subpage type rules
    parent_page_types = ['neighborhoods.HomePage']
    subpage_types = []


