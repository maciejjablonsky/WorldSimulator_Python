from organisms.plants.plant import Plant


class DeadlyNightshade(Plant):
    def __init__(self, world, strength=99, species="deadly nightshade"):
        super(Plant, self).__init__(world, strength, Plant.initiative, species)

    def collision(self, attacker):
        defender = self
        self.world.commentator.say(str(defender) + " was eaten by " + str(attacker))
        self.world.commentator.say(str(attacker) + " died after eating " + str(defender))
        attacker.die()
        defender.die()
