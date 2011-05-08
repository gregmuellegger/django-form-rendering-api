from django import forms
from django.utils.translation import ugettext_lazy as _


class ColorForm(forms.Form):
    color = forms.RegexField(label=_('Color'), regex=r'^#[a-fA-F0-9]{6}$')


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label=_('First name'),
        max_length=50,
        help_text=_(u'Enter your firstname'))
    last_name = forms.CharField(
        label=_('Last name'),
        max_length=50,
        help_text=_(u'Enter your surname.'))
    birthday = forms.DateField(_(u'Birthday'), required=False)
    email = forms.EmailField(label=_('Emailaddress'))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)


class LongForm(forms.Form):
    char1 = forms.CharField()
    char2 = forms.CharField()
    char3 = forms.CharField()
    char4 = forms.CharField()
    char5 = forms.CharField()
    integer1 = forms.IntegerField()
    integer2 = forms.IntegerField()
    integer3 = forms.IntegerField()
    integer4 = forms.IntegerField()
    integer5 = forms.IntegerField()
    date1 = forms.DateField()
    date2 = forms.DateField()
    date3 = forms.DateField()
    date4 = forms.DateField()
    date5 = forms.DateField()


class FieldTypeForm(forms.Form):
    boolean_field = forms.BooleanField()
    char_field = forms.CharField()
    choice_field = forms.ChoiceField()
    date_field = forms.DateField()
    date_time_field = forms.DateTimeField()
    decimal_field = forms.DecimalField()
    email_field = forms.EmailField()
    file_field = forms.FileField()
    float_field = forms.FloatField()
    integer_field = forms.IntegerField()
    ip_address_field = forms.IPAddressField()
    multiple_choice_field = forms.MultipleChoiceField()
    null_boolean_field = forms.NullBooleanField()
    slug_field = forms.SlugField()
    time_field = forms.TimeField()
    url_field = forms.URLField()
