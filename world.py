from random import randrange

from organisms.animals.human import Human
from species import species_dictionary


class World:
    def __init__(self, width, height, commentator):
        self.width = width
        self.height = height
        self.commentator = commentator
        self._organisms = []

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def commentator(self):
        return self._commentator

    @commentator.setter
    def commentator(self, commentator):
        self._commentator = commentator

    @property
    def organisms(self):
        return self._organisms

    def is_there_anybody(self, position):
        for organism in self.organisms:
            if organism.position == position:
                return True
        return False

    def empty_place(self, position):
        return not (self.is_there_anybody(position))

    def organism_at(self, position):
        for organism in self.organisms:
            if organism.position == position:
                return organism
        return None

    def human_alive(self):
        for organism in self._organisms:
            if isinstance(organism, Human):
                return True
        return False

    def destroy(self):
        self.organisms.clear()

    def delete_organism(self, organism):
        self.organisms.remove(organism)

    def create_organism(self, *args, **kwargs):
        if "plant_parent" in kwargs:
            plant_parent = kwargs["plant_parent"]
            new_plant = type(plant_parent)(self)
        elif "defender_parent" in kwargs and "attacker_parent" in kwargs:
            defender_parent = kwargs["defender_parent"]
            attacker_parent = kwargs["attacker_parent"]
            new_animal = type(defender_parent)(self)
            places_to_breed = []
            places_to_breed = defender_parent.where_to_move
            places_to_breed.extend(attacker_parent.where_to_move)
            for i in range(0, places_to_breed.count()):
                if self.is_there_anybody(places_to_breed[i]):
                    places_to_breed.remove(places_to_breed[i])
                    i -= 1
            if places_to_breed.count() > 0:
                place_to_breed = places_to_breed[randrange(0, places_to_breed.count())].copy()
                new_animal.position = place_to_breed.copy()
                new_animal.destination = place_to_breed.copy()
                self.organisms.append(new_animal)
                self.commentator.say(
                    "[{0:s}] {1:s} was born!".format(species_dictionary[new_animal.species]["prompt"],
                                                     new_animal.species))
