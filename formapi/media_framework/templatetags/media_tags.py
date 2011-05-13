from django import template


register = template.Library()


def _context_key(media_type):
    return '_media_%s' % media_type


class MediaNode(template.Node):
    '''
    Renders content that was previously injected into the context by the
    ``addmedia`` tag.

    Examples:
        {% media "css" %}

        {% media "js" %}
    '''

    def __init__(self, media_type):
        self.media_type = media_type

    def render(self, context):
        context_key = _context_key(self.media_type)
        if context_key in context:
            contents = context[context_key]
            output = ''.join(contents)
            del context[context_key]
            return output
        return ''

    @classmethod
    def parse(cls, parser, tokens):
        bits = tokens.split_contents()
        tag_name, media_type = bits
        return cls(media_type)


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
        context_key = _context_key(self.media_type)
        if context_key not in context:
            context[context_key] = []
        context[context_key].append(self.nodelist.render(context))
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
