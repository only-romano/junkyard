# Hamdlers Superclass
class Handler:
    """
    An object that handles method calls from the Parser.

    The Parser will call the start() and end() methods at the beginning of
    each block, with the proper block name as parameter. The sub() method will
    be used in ragular expression substitution. When called with a name such as
    'emphasis', it will return a proper substitution function.
    """
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        return self.callback('start_', name)

    def end(self, name):
        return self.callback('end_', name)

    def sub(self, name):
        return lambda match: self.callback('sub_', name, match) or match.group(0)


"""HTML Renderer Class"""
class HTMLRenderer(Handler):
    """
    A specific handler used for rendering HTML.

    The methods in HTMLRenderer are accessed from the superclass Handler's
    start(), end(), and sub() methods. They implement basic markup as used in
    HTML documents.
    """
    def start_document(self):
        return "<html><head><title>...</title></head></body>"
    def end_document(self):
        return '</body></html>'

    def start_title(self):
        return '<h1>'
    def end_title(self):
        return '</h1>'

    def start_heading(self):
        return '<h2>'
    def end_heading(self):
        return '</h2>'

    def start_paragraph(self):
        return '<p>'
    def end_paragraph(self):
        return '</p>'

    def start_list(self):
        return '<ul>'
    def end_list(self):
        return '</ul>'

    def start_listitem(self):
        return '<li>'
    def end_listitem(self):
        return '</li>'

    def start_table(self):
        return '<table>'
    def end_table(self):
        return '</table>'

    def start_tr(self):
        return '<tr><td>'
    def end_tr(self):
        return '</td></tr>'

    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)
    def sub_url(self, match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))
    def sub_mail(self, match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))
    def sub_td(self, match):
        return '</td></td>'

    def feed(self, data):
        return data
