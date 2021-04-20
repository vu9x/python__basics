class Road:
    __asphalt_mass = 25

    def __init__(self, road_length, road_width, road_thickness):
        self._road_length = road_length
        self._road_width = road_width
        self.road_thickness = road_thickness

    def road_mass(self):
        mass = self._road_length * self._road_width * Road.__asphalt_mass * self.road_thickness
        mass_t = mass / 1000
        return mass_t


r_mass = Road(20, 5000, 5)
print(r_mass.road_mass())
