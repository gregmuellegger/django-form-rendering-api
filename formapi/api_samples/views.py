from django.shortcuts import render_to_response
from django.template import RequestContext
from formapi.api_samples.forms import (RegistrationForm, VeryLongForm,
    FieldTypeForm)


def form_api_sample(request, template_name):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST, prefix='registration')
        very_long_form = VeryLongForm(request.POST, prefix='verylong')
        field_type_form = FieldTypeForm(request.POST, prefix='fieldtype')
    else:
        registration_form = RegistrationForm(prefix='registration')
        very_long_form = VeryLongForm(prefix='verylong')
        field_type_form = FieldTypeForm(prefix='fieldtype')
    return render_to_response(template_name, {
        'registration_form': registration_form,
        'very_long_form': very_long_form,
        'field_type_form': field_type_form,
    }, context_instance=RequestContext(request))
