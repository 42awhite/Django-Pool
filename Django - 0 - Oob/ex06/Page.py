#!/usr/bin/python3
from elem import Elem, Text
from elements import Html, Head, Body, Title, H1, H2, Div, Table, Tr, Th, Td, Ul, Ol, Li, P, Span

class Page:
    """Analizador y renderizador de páginas HTML con validación estructural."""

    def __init__(self, root_elem):
        if not isinstance(root_elem, Elem):
            raise TypeError("Root must be an instance of Elem.")
        self.root = root_elem

    def is_valid(self):
        """Verifica recursivamente si la estructura cumple las reglas del PDF."""
        return self.__recursive_check(self.root)

    def __recursive_check(self, node):
        # 1. Validamos el nodo actual según su tipo
        if not self.__check_node_rules(node):
            return False

        # 2. Si el nodo tiene hijos (y no es solo texto), validamos cada hijo
        if isinstance(node, Elem):
            for child in node.content:
                if isinstance(child, Elem):
                    if not self.__recursive_check(child):
                        return False
        return True

    def __check_node_rules(self, node):
        """Implementación de las reglas específicas del Subject."""

        # Html: debe tener exactamente un Head y un Body (en ese orden)
        if isinstance(node, Html):
            return (len(node.content) == 2 and
                    isinstance(node.content[0], Head) and
                    isinstance(node.content[1], Body))

        # Head: debe tener exactamente un Title
        if isinstance(node, Head):
            return len(node.content) == 1 and isinstance(node.content[0], Title)

        # Body y Div: solo H1, H2, Div, Table, Ul, Ol, Span o Text
        if isinstance(node, (Body, Div)):
            valid_types = (H1, H2, Div, Table, Ul, Ol, Span, Text)
            return all(isinstance(c, valid_types) for c in node.content)

        # Title, H1, H2, Li, Th, Td: solo un Text
        if isinstance(node, (Title, H1, H2, Li, Th, Td)):
            return len(node.content) == 1 and isinstance(node.content[0], Text)

        # P: solo Text
        if isinstance(node, P):
            return all(isinstance(c, Text) for c in node.content)

        # Span: solo Text o P
        if isinstance(node, Span):
            return all(isinstance(c, (Text, P)) for c in node.content)

        # Ul y Ol: al menos un Li, y solo Li
        if isinstance(node, (Ul, Ol)):
            return len(node.content) >= 1 and all(isinstance(c, Li) for c in node.content)

        # Tr: al menos un Th o Td (mutuamente exclusivos) y solo esos
        if isinstance(node, Tr):
            if len(node.content) < 1: return False
            first_type = type(node.content[0])
            if first_type not in (Th, Td): return False
            return all(isinstance(c, first_type) for c in node.content)

        # Table: solo Tr
        if isinstance(node, Table):
            return all(isinstance(c, Tr) for c in node.content)

        return True # Por defecto si no hay regla específica

    def __str__(self):
        """Renderiza el HTML. Añade DOCTYPE si la raíz es Html."""
        result = ""
        if isinstance(self.root, Html):
            result += "<!DOCTYPE html>\n"
        result += str(self.root)
        return result

    def write_to_file(self, filename):
        """Escribe el contenido en un archivo."""
        try:
            with open(filename, 'w') as f:
                f.write(str(self))
        except Exception as e:
            print(f"Error writing to file: {e}")

# --- Tests de demostración ---
if __name__ == '__main__':
    # Test 1: Página Perfecta
    ok_page = Page(Html([
        Head(Title(Text("Valid Page"))),
        Body([H1(Text("Hello World")), Div(Span(Text("Text")))])
    ]))
    print(f"Is OK page valid? {ok_page.is_valid()}") # True

    # Test 2: Página Corrupta (Body dentro de Body)
    bad_page = Page(Html([
        Head(Title(Text("Bad Page"))),
        Body([Body(Text("Error"))])
    ]))
    print(f"Is bad page valid? {bad_page.is_valid()}") # False
