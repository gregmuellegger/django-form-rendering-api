from django import forms
from django.utils.translation import ugettext_lazy as _


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


class VeryLongForm(forms.Form):
    field1 = forms.CharField()
    field2 = forms.CharField()
    field3 = forms.CharField()
    field4 = forms.CharField()
    field5 = forms.CharField()
    field6 = forms.CharField()
    field7 = forms.CharField()
    field8 = forms.CharField()
    field9 = forms.CharField()
    field10 = forms.CharField()
    field11 = forms.CharField()
    field12 = forms.CharField()
    field13 = forms.CharField()
    field14 = forms.CharField()
    field15 = forms.CharField()
    field16 = forms.CharField()
    field17 = forms.CharField()
    field18 = forms.CharField()
    field19 = forms.CharField()
    field20 = forms.CharField()
    field21 = forms.CharField()
    field22 = forms.CharField()
    field23 = forms.CharField()
    field24 = forms.CharField()
    field25 = forms.CharField()
    field26 = forms.CharField()
    field27 = forms.CharField()
    field28 = forms.CharField()
    field29 = forms.CharField()
    field30 = forms.CharField()
    field31 = forms.CharField()
    field32 = forms.CharField()
    field33 = forms.CharField()
    field34 = forms.CharField()
    field35 = forms.CharField()
    field36 = forms.CharField()
    field37 = forms.CharField()
    field38 = forms.CharField()
    field39 = forms.CharField()
    field40 = forms.CharField()


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
