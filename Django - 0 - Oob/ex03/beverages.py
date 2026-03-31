class HotBeverage:
    # Clase base para todas las bebidas calientes.
    def __init__(self, name="hot beverage", price=0.30):
        self.name = name
        self.price = price

    def description(self):
        # Devuelve la descripción básica de la bebida.
        return "Just some hot water in a cup."

    def __str__(self):
        # Método mágico para representar el objeto como cadena de texto.
        # Usamos f-strings para formatear el precio a 2 decimales.
        description = f"name: {self.name}\n"
        description += f"price: {self.price:.2f}\n"
        description += f"description: {self.description()}"
        return description

class Coffee(HotBeverage):
    # Hereda de HotBeverage y redefine sus atributos específicos.
    def __init__(self):
        self.name = "coffee"
        self.price = 0.40

    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    # Hereda de HotBeverage. Solo cambiamos el nombre.
    def __init__(self):
        # aquí simplemente sobreescribimos el atributo, precio igual.
        super().__init__(name="tea")

class Chocolate(HotBeverage):
    def __init__(self):
        self.name = "chocolate"
        self.price = 0.50

    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        self.name = "cappuccino"
        self.price = 0.45

    def description(self):
        return "Un po' di Italia nella sua tazza!"


def main_tests():
    beverages = [
        HotBeverage(),
        Coffee(),
        Tea(),
        Chocolate(),
        Cappuccino()
    ]

    for bev in beverages:
        print(bev)
        print("---")

if __name__ == "__main__":
    try:
        main_tests()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
