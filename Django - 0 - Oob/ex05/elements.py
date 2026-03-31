#!/usr/bin/python3
from elem import Elem, Text

# --- Etiquetas Estándar (Dobles) ---

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', attr=attr, content=content, tag_type='double')

class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='head', attr=attr, content=content, tag_type='double')

class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='body', attr=attr, content=content, tag_type='double')

class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='title', attr=attr, content=content, tag_type='double')

class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h1', attr=attr, content=content, tag_type='double')

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h2', attr=attr, content=content, tag_type='double')

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='div', attr=attr, content=content, tag_type='double')

class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='table', attr=attr, content=content, tag_type='double')

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='tr', attr=attr, content=content, tag_type='double')

class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='th', attr=attr, content=content, tag_type='double')

class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='td', attr=attr, content=content, tag_type='double')

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ul', attr=attr, content=content, tag_type='double')

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ol', attr=attr, content=content, tag_type='double')

class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='li', attr=attr, content=content, tag_type='double')

class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='p', attr=attr, content=content, tag_type='double')

class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='span', attr=attr, content=content, tag_type='double')

# --- Etiquetas Simples (Sin contenido) ---

class Hr(Elem):
    def __init__(self, content=None, attr={}):
        # Hr no debería tener contenido según el estándar HTML
        super().__init__(tag='hr', attr=attr, content=content, tag_type='simple')

class Br(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='br', attr=attr, content=content, tag_type='simple')


if __name__ == '__main__':
    # Test para demostrar que podemos montar una página rápido
    try:
        print(
            Html([
                Head(Title(Text("Página de prueba"))),
                Body([
                    H1(Text("¿Qué tal, Mentor?")),
                    P(Text("Esto es un párrafo.")),
                    Hr(),
                    Br(),
                    Div(Text("Un div final."))
                ])
            ])
        )
    except Exception as e:
        print(f"Error: {e}")
