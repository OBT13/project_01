class Plant:
    def __init__(self,name,height,age):
        self.name = name
        self.height = height
        self.age = age
    def grow(self):
        self.height += 1
    def age_day(self):
        self.age += 1
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

if __name__ == "__main__":
     # Create a Plant object named "rose" with initial height and age
    rose = Plant("Rose",25,30)

    # Save the initial height for comparison later
    last_height = rose.height

    # Simulate 6 days of growth (grow and age the plant)
    print("=== Day 1 ===")
    print(rose.get_info())


   
    for _ in range(6):
        rose.grow() # Plant grows 1cm per day
        rose.age_day()  # Plant ages by 1 day

    # Day 7: Display the updated status of the plant
    print("=== Day 7 ===")
    print(rose.get_info())

    # Calculate and display the growth in height during the week
    print(f"Growth this week: +{rose.height - last_height}cm")
