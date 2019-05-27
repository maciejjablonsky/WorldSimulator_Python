from organisms.organism import Organism
from point import Point
from random import randrange


class Animal(Organism):
    def __init__(self, world, strength, initiative, species):
        super(Organism, self).__init__(world, strength, initiative, species)

    def action(self):
        self.move_and_attack()

    def collision(self, attacker):
        if self.partner_of(attacker):
            self.world.create_animal(self, attacker)
        else:
            self.fight(attacker)

    def move_and_attack(self):
        attacker = self
        places = attacker.where_to_move
        place_to_move = places[randrange(0, places.count())].copy()
        attacker.destination = Point(place_to_move.x, place_to_move.y)
        if self.world.is_there_anybody(place_to_move):
            defender = self.world.organism_at(place_to_move)
            defender.collision(attacker)
            if attacker.alive and attacker.attack_in_process:
                attacker.move_to_destination()
        else:
            attacker.move_to_destination()

    @property
    def where_to_move(self):
        middle = self.position.copy()
        possible = Point(0, 0)
        places = []

        # up
        possible.set(Point(middle.x, middle.y - 1))
        if possible.y >= 0:
            places.append(possible.copy())
        # right
        possible.set(Point(middle.x + 1, middle.y))
        if possible.x < self.world.width:
            places.append(possible.copy)
        # down
        possible.set(Point(middle.x, middle.y + 1))
        if possible.y < self.world.height:
            places.append(possible.copy)
        # left
        possible.set(Point(middle.x - 1, middle.y))
        if possible.y >= 0:
            places.append(possible.copy())

        return places

    @property
    def attack_in_process(self):
        return self.position != self.destination

    def move_to_destination(self):
        self.position = self.destination

    def fight(self, attacker):
        defender = self
        if attacker.stronger_than(defender) or attacker.equally_strong_as(defender):
            defender.die()
            self.world.commentator.say(attacker + " killed " + defender + " during the attack")
        else:
            attacker.die()
            self.world.commentator.say(defender + " killed " + attacker + " in self defense")
