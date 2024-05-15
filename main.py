class PointSystem:
    def __init__(self):
        self.points = 0

    def add_points(self, amount):
        self.points += amount

    def deduct_points(self, amount):
        self.points -= amount
        if self.points < 0:
            self.points = 0  # Undgå negative point

    def get_points(self):
        return self.points

# Opret et PointSystem objekt
point_system = PointSystem()

# Eksempel: Tilføj 10 point
point_system.add_points(10)

# Eksempel: Fratræk 5 point
point_system.deduct_points(5)

# Udskriv antallet af point
print("Antal point:", point_system.get_points())

