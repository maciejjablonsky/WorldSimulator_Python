from random import uniform

from organisms.animals.animal import Animal


class Turtle(Animal):
    move_probability: float = 0.75
    resistance_level: int = 5

    def __init(self, world, strength=2, initiative=1, species="turtle"):
        super(Animal, self).__init__(world, strength, initiative, species)

    def action(self):
        if uniform(0, 1) < Turtle.move_probability:
            self.move_and_attack()

    def collision(self, attacker):
        defender = self
        if attacker.partner_of(defender):
            self.world.create_animal(self, attacker)
        else:
            if attacker.strength < Turtle.resistance_level:
                self.world.commentator.say(str(defender) + " bounced back the attack of " + str(attacker))
                attacker.destination = attacker.position
            else:
                self.fight(attacker)
