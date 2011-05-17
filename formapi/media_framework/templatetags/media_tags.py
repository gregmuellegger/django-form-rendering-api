from django import template


register = template.Library()


class MediaDict(dict):
    context_attribute = '_media'

    def __getitem__(self, key):
        return self.setdefault(key, [])

    def get_content(self, key):
        return self.pop(key, [])

    @classmethod
    def from_context(cls, context):
        if not hasattr(context.render_context, cls.context_attribute):
            setattr(context.render_context, cls.context_attribute, cls())
        return getattr(context.render_context, cls.context_attribute)


class MediaNode(template.Node):
    '''
    Renders content that was previously injected into the context by the
    ``addmedia`` tag.

    Examples:
        {% media "css" %}

        {% media "js" %}
    '''

    def __init__(self, media_type, nodelist):
        self.media_type = media_type
        self.nodelist = nodelist

    def render(self, context):
        media = MediaDict.from_context(context)
        contents = self.nodelist.render(context)
        output = []
        output.extend(media.get_content(self.media_type))
        output.append(contents)
        return ''.join(output)

    @classmethod
    def parse(cls, parser, tokens):
        bits = tokens.split_contents()
        tag_name, media_type = bits
        nodelist = parser.parse()
        return cls(media_type, nodelist)


class AddMediaNode(template.Node):
    '''
    Records the content between the ``addmedia`` and ``endaddmedia`` tags and
    injects the nodelist into the context.

    Examples:
        {% addmedia "css" %}
            <link rel="stylesheet" href="..." />
        {% endaddmedia "css" %}

        {% addmedia "js" %}
            <script type="text/javascript">
                alert("Hello World!");
            </script>
        {% endaddmedia "js" %}
    '''
    def __init__(self, media_type, nodelist):
        self.media_type = media_type
        self.nodelist = nodelist

    def render(self, context):
        media = MediaDict.from_context(context)
        media[self.media_type].append(self.nodelist.render(context))
        return ''

    @classmethod
    def parse(cls, parser, tokens):
        bits = tokens.split_contents()
        tag_name, media_type = bits
        nodelist = parser.parse(('end%s' % tag_name,))
        parser.delete_first_token()
        return cls(media_type, nodelist)


register.tag('media', MediaNode.parse)
register.tag('addmedia', AddMediaNode.parse)
