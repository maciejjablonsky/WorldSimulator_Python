from random import randrange

from organisms.animals.animal import Animal


class Fox(Animal):
    def __init__(self, world, strength=3, initiative=7, species="fox"):
        super(Animal, self).__init__(world, strength, initiative, species)

    def action(self):
        attacker = self
        places_to_move = attacker.where_to_move
        place_to_move = places_to_move[randrange(0, places_to_move.count())].copy()
        attacker.move_to_destination()
        while attacker.attack_in_process:
            if self.world.is_there_anybody(place_to_move):
                defender = attacker.who_is_defending(place_to_move)
                if attacker.strength > defender.strength:
                    defender.collision(attacker)
                    if attacker.alive and attacker.attack_in_process:
                        attacker.move_to_destination()
                else:
                    self.world.commentator.say(str(attacker) + " dodged fight with " + str(defender))
                    places_to_move.remove(place_to_move)
                    if places_to_move.count() > 0:
                        place_to_move = places_to_move[randrange(0, places_to_move.count())].copy()
                        attacker.destination = place_to_move
                    else:
                        attacker.destination = attacker.position
            else:
                attacker.move_to_destination()
