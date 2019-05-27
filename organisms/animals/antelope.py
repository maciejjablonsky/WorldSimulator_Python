from organisms.animals.animal import Animal
from random import uniform, randrange


class Antelope(Animal):
    escape_chance = 0.5

    def __init__(self, world, strength=4, initiative=4, species="sheep"):
        super(Animal, self).__init__(world, strength, initiative, species)

    def collision(self, attacker):
        if self.partner_of(attacker):
            self.world.create_animal(self, attacker)
        else:
            if uniform(0, 1) <= Antelope.escape_chance:
                escape_places = self.where_to_move
                while escape_places.count() > 0:
                    i = randrange(0, escape_places.count())
                    if self.world.is_there_anybody(escape_places[i]):
                        escape_places.remove(escape_places[i])
                    else:
                        self.destination = escape_places[i].copy()
                        self.move_to_destination()
                        self.world.commentator.say(self + " escaped from " + attacker)
                        break
                if escape_places.count() == 0:
                    self.fight(attacker)
            else:
                self.fight(attacker)

    def action(self):
        if not self.action_with_fight():
            self.action_with_fight()

    def action_with_fight(self):
        met_someone = False
        attacker = self
        places_to_move = attacker.where_to_move
        place_to_move = places_to_move[randrange(0, places_to_move.count())].copy()
        attacker.destination = place_to_move
        if self.world.is_there_anybody(place_to_move):
            met_someone = True
            defender = attacker.who_is_defending(place_to_move)
            defender.collision(attacker)
            if attacker.alive and attacker.attack_in_process:
                attacker.move_to_destination()
        else:
            self.move_to_destination()

        return met_someone
