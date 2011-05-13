import re
from django.template.loader import render_to_string
from django.template import Context, Template
from django.test import TestCase


WHITESPACE = re.compile('\s+')


class IgnoreWhitespaceTestCase(TestCase):
    def assertEqualExceptWhitespace(self, first, second, msg=None):
        first = WHITESPACE.sub('', first)
        second = WHITESPACE.sub('', second)
        super(IgnoreWhitespaceTestCase, self).assertEqual(first, second, msg)


class MediaRenderTests(IgnoreWhitespaceTestCase):
    def test_template_lib_exists(self):
        Template('{% load media_tags %}')

    def test_media_tag_should_compile(self):
        Template('{% load media_tags %}{% media "css" %}')

    def test_media_tag_outputs_recorded_content(self):
        t = Template('''
        {% load media_tags %}
        {% addmedia "css" %}
        <style type="text/css">
            html { display: none; }
        </style>
        {% endaddmedia %}

        before media
        {% media "css" %}
        after media
        ''')
        output = t.render(Context())
        self.assertEqualExceptWhitespace(output, '''
            before media
            <style type="text/css">
                html { display: none; }
            </style>
            after media
            ''')

    def test_media_tag_outputs_recorded_content_even_before_the_content_is_defined(self):
        t = Template('''
        {% load media_tags %}

        before media
        {% media "css" %}
        after media

        {% addmedia "css" %}
        <style type="text/css">
            html { display: none; }
        </style>
        {% endaddmedia %}
        ''')
        output = t.render(Context())
        self.assertEqualExceptWhitespace(output, '''
            before media
            <style type="text/css">
                html { display: none; }
            </style>
            after media
            ''')


class InheritanceTests(IgnoreWhitespaceTestCase):
    def test_simple_inheritance(self):
        context = {}
        output = render_to_string(
            'media_framework/tests/test_simple_inheritance.html',
            context)
        expected = render_to_string(
            'media_framework/tests/test_simple_inheritance.expect.html',
            context)
        self.assertEqualExceptWhitespace(output, expected)
