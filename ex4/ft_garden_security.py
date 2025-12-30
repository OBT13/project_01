class GardenSecurity:
    def __init__(self, name ,height, age):
        self.name = name
        self._height = height
        self._age = age
    def set_height(self, height):
        if(height >= 0):
            self._height = height
            print(f"Height updated: {self._height}cm [OK]\n")
        else:
            print("Security: Negative height rejected\n")

    def get_height(self):
        return self._height
    
    def set_age(self, age):
        if(age >= 0):
            self._age = age
            print(f"Age updated: {self._age} days [OK]")
        else:
            print("Security: Negative age rejected\n")
    def get_age(self):
        return self._age
    def display_info(self):
        print(f"Current plant: {self.name} ({self._height}cm, {self._age} days)")

if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = GardenSecurity("Rose",88,77)
    print(f"Plant created: {plant.name}")

    plant.set_age(30)
    plant.set_height(25)


    print("Invalid operation attempted: height -5cm [REJECTED]")
    plant.set_height(-5)

    plant.display_info()
    