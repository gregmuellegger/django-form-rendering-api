from django.shortcuts import render_to_response
from django.template import RequestContext
from formapi.api_samples.forms import (ColorForm, RegistrationForm,
    LongForm, FieldTypeForm)


def form_api_sample(request, template_name):
    if request.method == 'POST':
        color_form = ColorForm(request.POST, prefix='registration')
        registration_form = RegistrationForm(request.POST, prefix='registration')
        long_form = LongForm(request.POST, prefix='long')
        field_type_form = FieldTypeForm(request.POST, prefix='fieldtype')
    else:
        color_form = ColorForm(prefix='registration')
        registration_form = RegistrationForm(prefix='registration')
        long_form = LongForm(prefix='long')
        field_type_form = FieldTypeForm(prefix='fieldtype')
    return render_to_response(template_name, {
        'color_form': color_form,
        'registration_form': registration_form,
        'long_form': long_form,
        'field_type_form': field_type_form,
    }, context_instance=RequestContext(request))
