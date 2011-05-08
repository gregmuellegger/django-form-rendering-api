from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import loader


def show_template(request, template_name):
    if not loader.template_source_loaders:
        try:
            loader.find_template(template_name)
        except loader.TemplateDoesNotExist:
            raise Http404
    source = None
    for template_loader in loader.template_source_loaders:
        try:
            source = template_loader.load_template_source(template_name)
        except loader.TemplateDoesNotExist:
            pass
    if source is None:
        raise Http404
    return render_to_response('show_template.html', {
        'template_source': source[0],
    }, context_instance=RequestContext(request))
