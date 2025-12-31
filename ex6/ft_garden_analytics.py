class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.initial_height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = False

    def bloom(self):
        self.blooming = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points


class GardenManager:
    garden_count = 0

    class GardenStats:
      
        def total_growth(plants):
            return sum(p.height - p.initial_height for p in plants)

        def count_types(plants):
            regular = flowering = prize = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize
 

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        GardenManager.garden_count += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(
                    f"- {plant.name}: {plant.height}cm, "
                    f"{plant.color} flowers (blooming), "
                    f"Prize points: {plant.prize_points}"
                )
            elif isinstance(plant, FloweringPlant):
                print(
                    f"- {plant.name}: {plant.height}cm, "
                    f"{plant.color} flowers (blooming)"
                )
            else:
                print(f"- {plant.name}: {plant.height}cm")

        total_growth = self.GardenStats.total_growth(self.plants)
        regular, flowering, prize = self.GardenStats.count_types(self.plants)

        print(
            f"\nPlants added: {len(self.plants)}, "
            f"Total growth: {total_growth}cm"
        )
        print(
            f"Plant types: {regular} regular, "
            f"{flowering} flowering, {prize} prize flowers"
        )


    def create_garden_network(cls):
        return cls.garden_count

    def validate_height(height):
        return height >= 0


def garden_score(plants):
    score = 0
    for p in plants:
        score += p.height
        if isinstance(p, PrizeFlower):
            score += p.prize_points
    return score
if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    # Creating garden managers
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    # Creating plants
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    # Adding plants to Alice's garden
    rose.bloom()
    sunflower.bloom()

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    # Growing plants and generating a report
    alice.grow_all()
    alice.report()

    # Height validation test
    print("\nHeight validation test:", GardenManager.validate_height(10))

    # Calculating garden scores
    alice_score = garden_score(alice.plants)
    bob_score = garden_score(bob.plants)

    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    # Total gardens managed
    print("Total gardens managed:", GardenManager.create_garden_network(GardenManager))
    