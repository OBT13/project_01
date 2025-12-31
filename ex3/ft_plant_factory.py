class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    # Create instances of the Plant class
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    # Display information about each plant
    print("=== Plant Factory Output ===")
    rose.display_info()
    oak.display_info()
    cactus.display_info()
    sunflower.display_info()
    fern.display_info()

    # Display the total number of plants created
    print("\nTotal plants created: 5")
