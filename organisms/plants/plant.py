from random import uniform

from organisms.organism import Organism
from point import Point


class Plant(Organism):
    seed_probability = 0.5
    plant_initiative = 0

    @property
    def places_to_seed(self):
        possible = Point(x=0, y=0)
        mid = self.position
        _places_to_seed = []
        # left
        possible.set(x=mid.x - 1, y=mid.y)
        if possible.x >= 0 and not self.world.is_there_anybody(possible):
            _places_to_seed.append(possible.copy())
        # right
        possible.set(x=mid.x + 1, y=mid.y)
        if possible.x < self.world.width and not self.world.is_there_anybody(possible):
            _places_to_seed.append(possible.copy())
        # up
        possible.set(x=mid.x, y=mid.y - 1)
        if possible.y >= 0 and not self.world.is_there_anybody(possible):
            _places_to_seed.append(possible.copy())
        # down
        possible.set(x=mid.x, y=mid.y + 1)
        if possible.y < self.world.height and not self.world.is_there_anybody(possible):
            _places_to_seed.append(possible.copy())
        return _places_to_seed

    def __init__(self, world, strength, species):
        super(Organism, self).__init__(world, strength, Plant.plant_initiative, species)

    def action(self):
        if uniform(0, 1) <= Plant.seed_probability:
            self.world.create_organism(plant_parent=self)

    def collision(self, attacker):
        defender = self
        self.world.commentator.say(str(defender) + " was eaten by " + str(attacker))
        defender.die()
