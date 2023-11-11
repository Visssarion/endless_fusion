class Ability:
    energy: int
    required_energy: int

    def __init__(self, required_energy: int):
        self.required_energy = required_energy
        self.energy = 0

    def add_energy(self, energy: int):
        self.energy += energy

    def get_coefficient(self):
        return self.energy / self.required_energy

    def can_be_activated(self):
        return self.energy >= self.required_energy

    def reset(self):
        self.energy = 0
