from organisms.plants.plant import Plant


class Guarana(Plant):
    strength_bonus = 3

    def __init__(self, world, strength=0, species="guarana"):
        super(Plant, self).__init__(world, strength, Plant.initiative, species)

    def collision(self, attacker):
        defender = self
        attacker.strength += Guarana.strength_bonus
        self.world.commentator.say(str(attacker) + " got strength bonus after eating " + str(defender))
        self.world.commentator.say(str(defender) + " was eaten by " + str(attacker))
        defender.die()
