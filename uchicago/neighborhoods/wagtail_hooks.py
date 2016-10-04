from django.conf import settings

from wagtail.wagtailcore import hooks

@hooks.register('insert_editor_js')
def editor_js():
    return '<script src="'+settings.STATIC_URL+'blocks/js/drawApp.js"></script><script src="'+settings.STATIC_URL+'blocks/vendor/js/d3.min.js"></script><script src="'+settings.STATIC_URL+'blocks/vendor/js/leaflet.js"></script><script src="'+settings.STATIC_URL+'blocks/vendor/js/leaflet.draw.js"></script></script>'


@hooks.register('insert_editor_css')
def editor_css():
    return '<link rel="stylesheet" href="'+settings.STATIC_URL+'blocks/vendor/css/leaflet.css" /><link rel="stylesheet" href="'+settings.STATIC_URL+'blocks/vendor/css/leaflet.draw.css" /><link rel="stylesheet" href="'+settings.STATIC_URL+'blocks/css/drawApp.css" />'
