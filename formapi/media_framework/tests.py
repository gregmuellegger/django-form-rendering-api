import re
from django.template import Context, Template
from django.test import TestCase


WHITESPACE = re.compile('\s+')


class MediaRenderTests(TestCase):
    def assertEqual(self, first, second, msg=None, ignore_whitespace=False):
        if ignore_whitespace:
            first = WHITESPACE.sub('', first)
            second = WHITESPACE.sub('', second)
        super(MediaRenderTests, self).assertEqual(first, second, msg)

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
        self.assertEqual(output, '''
            before media
            <style type="text/css">
                html { display: none; }
            </style>
            after media
            ''', ignore_whitespace=True)
