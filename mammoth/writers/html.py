from __future__ import unicode_literals

import cgi


class HtmlWriter(object):
    def __init__(self):
        self._fragments = []
        self.break_after_start = [ 'p', 'ul', 'ol' ];
        self.break_after_end = [ 'p', 'ul', 'ol', 'li' ];
    
    def text(self, text):
        self._fragments.append(_escape_html(text))
    
    def start(self, name, attributes=None):
        attribute_string = _generate_attribute_string(attributes)
        self._fragments.append("<{0}{1}>".format(name, attribute_string))
        if name in self.break_after_start:
            self._fragments.append("\n")

    def end(self, name):
        self._fragments.append("</{0}>".format(name))
        if name in self.break_after_end:
            self._fragments.append("\n")
    
    def self_closing(self, name, attributes=None):
        attribute_string = _generate_attribute_string(attributes)
        self._fragments.append("<{0}{1} />".format(name, attribute_string))
    
    def append(self, html):
        self._fragments.append(html)
    
    def as_string(self):
        return "".join(self._fragments)


def _escape_html(text):
    return cgi.escape(text, quote=True)


def _generate_attribute_string(attributes):
    if attributes is None:
        return ""
    else:
        return "".join(
            ' {0}="{1}"'.format(key, _escape_html(attributes[key]))
            for key in sorted(attributes)
        )
