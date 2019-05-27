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

    def create_animal(self, local_parent, invading_parent):
        new_animal = type(local_parent)(self)
        places_to_breed = local_parent.where_to_move
        places_to_breed.extend(invading_parent.where_to_move)
        self.organisms.append(new_animal)
        self.commentator.say(
            "[{0:s}] {1:s} was born!".format(species_dictionary[new_animal.species]["prompt"], new_animal.species))
