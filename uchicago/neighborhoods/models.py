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

class LandingPage(Page):
  body = RichTextField(blank=True)

  content_panels = Page.content_panels + [
    FieldPanel('body', classname="full")
  ]

# model class for map drawing tools
class DrawMapBlock(blocks.StructBlock):
	idNum = models.AutoField(primary_key=False)
	drawnNeighborhood = blocks.TextBlock()

	class Meta:
		form_classname = 'map-block struct-block'
		icon = 'site'
		label = 'Draw Tools'
		form_template = 'blocks/map.html'
		template = 'blocks/json.html'

class ChicagoNeighborhoods(Page):

	# Database fields
	neighborhood_name = models.CharField(max_length=255, default='', null=False, blank=False)
	date = models.DateField("Updated On")
	introductory_text = models.CharField(max_length=255, default='', null=False, blank=False)
	introductory_image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	overview = StreamField([
		('draw', DrawMapBlock()),
		('heading', blocks.CharBlock(classname="heading")),
		('paragraph', blocks.RichTextBlock()),
		('image', ImageChooserBlock()),
		('video', EmbedBlock()),
		('document', DocumentChooserBlock()),
	], default='')
	social_mix = StreamField([
		('draw', DrawMapBlock()),
		('heading', blocks.CharBlock(classname="heading")),
		('paragraph', blocks.RichTextBlock()),
		('image', ImageChooserBlock()),
		('video', EmbedBlock()),
		('document', DocumentChooserBlock()),
	])
	public_space = StreamField([
		('draw', DrawMapBlock()),
		('heading', blocks.CharBlock(classname="heading")),
		('paragraph', blocks.RichTextBlock()),
		('image', ImageChooserBlock()),
		('video', EmbedBlock()),
		('document', DocumentChooserBlock()),
	])
	amenities = StreamField([
		('draw', DrawMapBlock()),
		('heading', blocks.CharBlock(classname="heading")),
		('paragraph', blocks.RichTextBlock()),
		('image', ImageChooserBlock()),
		('video', EmbedBlock()),
		('document', DocumentChooserBlock()),
	])
	connections = StreamField([
		('draw', DrawMapBlock()),
		('heading', blocks.CharBlock(classname="heading")),
		('paragraph', blocks.RichTextBlock()),
		('image', ImageChooserBlock()),
		('video', EmbedBlock()),
		('document', DocumentChooserBlock()),
	])
	final_project = StreamField([
		('draw', DrawMapBlock()),
		('heading', blocks.CharBlock(classname="heading")),
		('paragraph', blocks.RichTextBlock()),
		('image', ImageChooserBlock()),
		('video', EmbedBlock()),
		('document', DocumentChooserBlock()),
	])

	# Search index configuraiton
	search_fields = Page.search_fields + [
		index.SearchField('neighborhood_name'),
		index.SearchField('introductory_text'),
		index.SearchField('overview'),
		index.SearchField('social_mix'),
		index.SearchField('public_space'),
		index.SearchField('amenities'),
		index.SearchField('connections'),
		index.SearchField('final_project'),
		index.FilterField('date'),
	]

	# Editor panels configuration
	content_panels = Page.content_panels + [
		FieldPanel('neighborhood_name'),
		FieldPanel('introductory_text'),
		ImageChooserPanel('introductory_image'),
		StreamFieldPanel('overview'),
		StreamFieldPanel('social_mix'),
		StreamFieldPanel('public_space'),
		StreamFieldPanel('amenities'),
		StreamFieldPanel('connections'),
		StreamFieldPanel('final_project'),
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
	city_beautiful = StreamField([
		('heading', blocks.CharBlock(classname="heading")),
		('paragraph', blocks.RichTextBlock()),
		('image', ImageChooserBlock()),
		('video', EmbedBlock()),
		('document', DocumentChooserBlock()),
		('draw', DrawMapBlock()),
	])
	transects = StreamField([
		('heading', blocks.CharBlock(classname="heading")),
		('paragraph', blocks.RichTextBlock()),
		('image', ImageChooserBlock()),
		('video', EmbedBlock()),
		('document', DocumentChooserBlock()),
		('draw', DrawMapBlock()),
	])
	diversity = StreamField([
		('heading', blocks.CharBlock(classname="heading")),
		('paragraph', blocks.RichTextBlock()),
		('image', ImageChooserBlock()),
		('video', EmbedBlock()),
		('document', DocumentChooserBlock()),
		('draw', DrawMapBlock()),
	])
	civic_art = StreamField([
		('heading', blocks.CharBlock(classname="heading")),
		('paragraph', blocks.RichTextBlock()),
		('image', ImageChooserBlock()),
		('video', EmbedBlock()),
		('document', DocumentChooserBlock()),
		('draw', DrawMapBlock()),
	])
	final_project = StreamField([
		('heading', blocks.CharBlock(classname="heading")),
		('paragraph', blocks.RichTextBlock()),
		('image', ImageChooserBlock()),
		('video', EmbedBlock()),
		('document', DocumentChooserBlock()),
		('draw', DrawMapBlock()),
	])

	# Search index configuraiton
	search_fields = Page.search_fields + [
		index.SearchField('introductory_text'),
		index.SearchField('city_beautiful'),
		index.SearchField('transects'),
		index.SearchField('diversity'),
		index.SearchField('civic_art'),
		index.SearchField('final_project'),
		index.FilterField('date'),
	]

	# Editor panels configuration
	content_panels = Page.content_panels + [
		FieldPanel('introductory_text'),
		ImageChooserPanel('introductory_image'),
		StreamFieldPanel('city_beautiful'),
		StreamFieldPanel('transects'),
		StreamFieldPanel('diversity'),
		StreamFieldPanel('civic_art'),
		StreamFieldPanel('final_project'),
		FieldPanel('date'),
	]

	edit_handler = TabbedInterface([
		ObjectList(content_panels, heading='Content'),
	])

	# Parent page / subpage type rules
	parent_page_types = ['neighborhoods.HomePage']
	subpage_types = []


