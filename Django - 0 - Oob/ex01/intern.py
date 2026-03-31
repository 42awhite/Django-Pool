class Intern:
    # Clase anidada o definida en el mismo ámbito para el café
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        # El constructor asigna el nombre o el valor por defecto
        self.Name = name

    def __str__(self):
        # Devuelve el atributo Name al imprimir la instancia
        return self.Name

    def work(self):
        # Lanza una excepción de tipo básico Exception
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        # Devuelve una instancia de la clase Coffee
        return self.Coffee()

if __name__ == "__main__":
    # 1. Instanciar becarios
    nobody = Intern()
    mark = Intern("Mark")

    # 2. Mostrar nombres
    print(nobody)
    print(mark)

    # 3. Mark hace café
    try:
        coffee = mark.make_coffee()
        print(coffee)
    except Exception as e:
        print(e)

    # 4. El otro becario intenta trabajar (y falla) [cite: 96]
    try:
        nobody.work()
    except Exception as e:
        # Gestionamos la excepción para que el programa no muera [cite: 96]
        print(e)
