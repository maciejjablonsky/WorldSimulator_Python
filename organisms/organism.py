import time

from point import Point


class Organism:
    def __init__(self, world, strength, initiative, species):
        self._creation_time = time.time()
        self._world = world
        self._strength = strength
        self._initiative = initiative
        self._species = species
        self._alive = True
        self._position = None
        self._destination = None

        for i in range(0, world.width * world.height):
            place = Point(x=0, y=0).randomize(world.width, world.height)
            if world.empty_place(place):
                self.position = place
                self.destination = place
                break

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        self._strength = strength

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, destination):
        self._destination = destination

    @property
    def initiative(self):
        return self._initiative

    @property
    def world(self):
        return self._world

    @property
    def age(self):
        return time.time() - self._creation_time

    @property
    def alive(self):
        return self._alive

    @property
    def dead(self):
        return not self.alive

    @property
    def species(self):
        return self._species

    def action(self):
        pass

    def collision(self, attacker):
        pass

    def die(self):
        self._alive = False
        self.world.delete_organism(self)

    def __str__(self):
        return "{0:s} at {1:s}".format(self.species, self.position)

    # TODO check proper order in __gt__

    def __gt__(self, another):
        if self.initiative == another.initiative:
            return self.age < another.age
        else:
            return self.initiative < another.initiative

    def partner_of(self, organism):
        return self.__class__ == organism.__class__

    def stronger_than(self, organism):
        return self.strength > organism.strength

    def equally_strong_as(self, organism):
        return self.strength == organism.strength

    def who_is_defending(self, position):
        return self.world.organism_at(position)
    
    def who_is_attacking(self):
        for organism in self.world.organisms:
            if organism.destination == self.position:
                return organism
        return None

    def distance_to(self, organism):
        return self.position.distance_to(organism.position)
