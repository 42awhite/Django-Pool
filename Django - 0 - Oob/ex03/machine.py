import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:

    class EmptyCup(HotBeverage):
        # Representa una taza vacía servida por error.
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        # Excepción lanzada cuando la máquina requiere reparación.
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self):
        # Contador para rastrear la obsolescencia (10 usos)
        self.served_count = 0
        self.is_broken = False

    def repair(self):
        #Reinicia el contador y repara la máquina.
        self.served_count = 0
        self.is_broken = False
        print("--- Machine repaired! ---")

    def serve(self, beverage_class: HotBeverage):
        #Sirve una bebida o una taza vacía.
        #Lanza BrokenMachineException si está rota
        if self.is_broken or self.served_count >= 10:
            self.is_broken = True
            raise self.BrokenMachineException()

        self.served_count += 1

        # 50% de probabilidad de servir la bebida o la taza vacía
        if random.choice([True, False]):
            return beverage_class()
        else:
            return self.EmptyCup()


def start_machine_tests():
    machine = CoffeeMachine()
    # Lista de clases (no instancias) para pedir
    beverage_types = [Coffee, Tea, Chocolate, Cappuccino]

    # Probamos dos ciclos de rotura
    for cycle in range(2):
        print(f"\n--- Starting Cycle {cycle + 1} ---")
        try:
            while True:
                bev_class = random.choice(beverage_types)
                served = machine.serve(bev_class)
                print(served)
                print(machine.served_count)
                print("-" * 10)
        except CoffeeMachine.BrokenMachineException as e:
            print(f"Error: {e}")
            machine.repair()

if __name__ == "__main__":
    try:
        start_machine_tests()
    except Exception as e:
        print(f"Fatal error in testing: {e}")
