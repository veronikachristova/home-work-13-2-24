class Pasta:
    def __init__(self, pasta_type):
        self.pasta_type = pasta_type
        self.sauce = None
        self.topping = None
        self.dressing = None

    def add_sauce(self, sauce):
        self.sauce = sauce

    def add_topping(self, topping):
        self.topping = topping

    def add_dressing(self, dressing):
        self.dressing = dressing


class Spaghetti(Pasta):
    def __init__(self):
        super().__init__("Spaghetti")


class Penne(Pasta):
    def __init__(self):
        super().__init__("Penne")


class Fettuccine(Pasta):
    def __init__(self):
        super().__init__("Fettuccine")


class PastaFactory:
    @staticmethod
    def create_pasta(pasta_type):
        if pasta_type == "Spaghetti":
            return Spaghetti()
        elif pasta_type == "Penne":
            return Penne()
        elif pasta_type == "Fettuccine":
            return Fettuccine()
        else:
            return None


if __name__ == "__main__":
    pasta1 = PastaFactory.create_pasta("Spaghetti")
    pasta1.add_sauce("Tomato Sauce")
    pasta1.add_topping("Parmesan Cheese")
    pasta1.add_dressing("Olive Oil")

    pasta2 = PastaFactory.create_pasta("Penne")
    pasta2.add_sauce("Alfredo Sauce")
    pasta2.add_topping("Grilled Chicken")
    pasta2.add_dressing("Basil Pesto")

    print(f"Pasta 1: {pasta1.pasta_type}, Sauce: {pasta1.sauce}, Topping: {pasta1.topping}, Dressing: {pasta1.dressing}")
    print(f"Pasta 2: {pasta2.pasta_type}, Sauce: {pasta2.sauce}, Topping: {pasta2.topping}, Dressing: {pasta2.dressing}")
