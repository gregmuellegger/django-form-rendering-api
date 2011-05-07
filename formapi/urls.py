from django.conf.urls.defaults import patterns, include, url
from django.shortcuts import render_to_response
from django.template import RequestContext

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

def index(request):
    return render_to_response('index.html', {
    }, context_instance=RequestContext(request))

urlpatterns = patterns('',
     url(r'^$', index),

     url(r'^legacy/$', 'formapi.api_samples.views.form_api_sample',
         {'template_name': 'api_samples/legacy.html'}),
     url(r'^single-tag/$', 'formapi.api_samples.views.form_api_sample',
         {'template_name': 'api_samples/single_tag.html'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
