class Animal:
    def __init__(self):
        self.value = 10

    def return_value(self):
        return self.value


class Rabbit(Animal):
    def __init__(self):
        super().__init__()


    def print_value(self):
        print(super().return_value())


rabbit1 = Rabbit()

rabbit1.print_value()