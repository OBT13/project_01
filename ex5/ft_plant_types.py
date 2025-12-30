class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name}  is blooming beautifully!\n")
    

class Tree(Plant):
    def __init__(self, name, height, age,trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {int(shade)} square meters of shade\n")

    

class Vegetable(Plant):
    def __init__(self, name, height, age,harvest_season,nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    def get_nutritional_value(self):
        print(f"{self.name} is rich in {self.nutritional_value}\n")




if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 400, 1500, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 70, "winter", "vitamin A")

    print(f"{rose.name} (Flower): {rose.height}cm, {rose.age} days, {rose.color} color")
    rose.bloom()

    print(f"{tulip.name} (Flower): {tulip.height}cm, {tulip.age} days, {tulip.color} color")
    tulip.bloom()

    print(f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()

    print(f"{pine.name} (Tree): {pine.height}cm, {pine.age} days, {pine.trunk_diameter}cm diameter")
    pine.produce_shade()

    print(f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days, {tomato.harvest_season} harvest")
    tomato.get_nutritional_value()

    print(f"{carrot.name} (Vegetable): {carrot.height}cm, {carrot.age} days, {carrot.harvest_season} harvest")
    carrot.get_nutritional_value()