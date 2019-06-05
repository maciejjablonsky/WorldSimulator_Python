from organisms.animals.animal import Animal
from organisms.animals.cybersheep import Cybersheep
from organisms.plants.plant import Plant
from point import Point


class Sosnowskihogweed(Plant):
    def __init__(self, world, strength=10, species="sosnowski hogweed"):
        super(Plant, self).__init__(world, strength, Plant.initiative, species)
        self._animal_neighbours = []

    @property
    def animal_neighbours(self):
        return self._animal_neighbours

    def _add_neighbour_to_vector(self, pos):
        neighbour = self.world.organism_at(pos)
        if neighbour != None and isinstance(neighbour, Animal):
            self._animal_neighbours.append(neighbour)

    def find_animal_neighbours(self):
        self._animal_neighbours.clear()
        pos = Point(self.position.copy)

        # up
        pos.set(x=self.position.x, y=self.position.y - 1)
        if pos.y >= 0 and self.world.is_there_anybody(pos):
            self._add_neighbour_to_vector(pos)
        # right
        pos.set(x=self.position.x + 1, y=self.position.y)
        if pos.x < self.world.width and self.world.is_there_anybody(pos):
            self._add_neighbour_to_vector(pos)
        # down
        pos.set(x=self.position.x, y=self.position.y + 1)
        if pos.y < self.world.height and self.world.is_there_anybody(pos):
            self._add_neighbour_to_vector(pos)
        # left
        pos.set(x=self.position.x - 1, y=self.position.y)
        if pos.x >= 0 and self.world.is_there_anybody(pos):
            self._add_neighbour_to_vector(pos)

    def action(self):
        self.find_animal_neighbours()
        for animal in self.animal_neighbours:
            if isinstance(animal, Cybersheep):
                self.world.commentator.say(str(animal) + " survived attack of " + str(self))
            else:
                self.world.commentator.say(str(animal) + " killed by " + str(self))
                animal.die()
        self.world.create_organism(plant_parent=self)

    def collision(self, attacker):
        defender = self
        self.world.commentator.say(str(defender) + " was eaten by " + str(attacker))
        defender.die()
        if isinstance(attacker, Cybersheep):
            self.world.commentator.say(str(attacker) + " ate " + str(defender))
        else:
            self.world.commentator.say(str(attacker) + " died after eating " + str(defender))
            attacker.die()
