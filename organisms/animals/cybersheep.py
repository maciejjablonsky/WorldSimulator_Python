from organisms.animals.sheep import Sheep
from point import Point


class Cybersheep(Sheep):
    def __init__(self, world, strength=11, initiative=4, species="cyber sheep"):
        super(Sheep, self).__init__(world, strength, initiative, species)

    @property
    def nearest_sosnowski(self):
        attacker = self
        min = 0
        distance = 0
        nearest_sosnowski = None
        for organism in self.world.organisms:
            if isinstance(organism, SosnowskiHogweed):
                distance = attacker.distance_to(organism)
                if nearest_sosnowski is None:
                    nearest_sosnowski = organism
                    min = distance
                elif distance < min:
                    nearest_sosnowski = organism
                    min = distance
        return nearest_sosnowski

    def action(self):
        attacker = self
        nearest_sosnowski = self.nearest_sosnowski
        self.world.commentator.say(attacker + " is going to eat the nearest " + nearest_sosnowski)
        place_to_move = Point(self.position)
        if nearest_sosnowski is not None:
            if attacker.position.greater_distance_is_in_x(nearest_sosnowski.position):
                if nearest_sosnowski.position.x > attacker.position.x:
                    place_to_move.x += 1
                else:
                    place_to_move.x -= 1
            else:
                if nearest_sosnowski.position.y > attacker.position.y:
                    place_to_move.y += 1
                else:
                    place_to_move.y -= 1

            attacker.destination = place_to_move

            if self.world.is_there_anybody(place_to_move):
                defender = attacker.who_is_defending(place_to_move)
                defender.collision(attacker)
                if attacker.alive and attacker.attack_in_process:
                    attacker.move_to_destination()
            else:
                attacker.move_to_destination()
        else:
            attacker.move_and_attack()

