from organisms.animals.animal import Animal
from point import Point


class Human(Animal):
    strength_bonus_value: int = 5
    super_power_duration: int = 5

    def __init__(self, world, strength=5, initiative=4, species="human"):
        super(Animal, self).__init__(world, strength, initiative, species)
        self._strength_bonus = 0
        self._round_counter = 0
        self._next_position = Point(x=0, y=0)

    @property
    def strength(self):
        return self.strength + self._strength_bonus

    @property
    def strength_bonus(self):
        return self._strength_bonus

    @strength_bonus.setter
    def strength_bonus(self, strength_bonus):
        self._strength_bonus = strength_bonus

    def action(self):
        attacker = self
        if self.next_position.x + self.position.x < 0:
            self.position = self.position.x + 1, self.position.y
        elif self.next_position.x + self.position.x >= self.world.width:
            self.position = self.position.x - 1, self.position.y
        if self.next_position.y + self.position.y < 0:
            self.position = self.position.x, self.position.y - 1
        elif self.next_position.y + self.position.y >= self.world.height:
            self.position = self.position.x, self.position.y - 1
        place_to_move = Point(self.position.x + self.next_position.x, self.position.y + self.next_position.y)
        self.destination = place_to_move
        if self.world.is_there_anybody(place_to_move):
            defender = self.who_is_defending(place_to_move)
            defender.collision(attacker)
            if attacker.alive and attacker.attack_in_process:
                attacker.move_to_destination()
        else:
            attacker.move_to_destination()
        attacker.process_super_power()

    @property
    def next_position(self):
        return self._next_position

    @next_position.setter
    def next_position(self, next_position):
        self._next_position = next_position

    @property
    def round_counter(self):
        return self._round_counter

    @round_counter.setter
    def round_counter(self, round_counter):
        self._round_counter = round_counter

    def use_super_power(self):
        if self.round_counter == 0:
            self.world.commentator.say(str(self) + " used the super power!")
            self.strength_bonus += Human.strength_bonus
            self.round_counter += Human.super_power_duration
        else:
            self.world.commentator.say(str(self) + " needs to wait to use the super power")

    def process_super_power(self):
        if self.round_counter > 0:
            self.round_counter -= 1
        if self.strength_bonus > 0:
            self.strength_bonus -= 1
            self.world.commentator.say(
                str(self) + " has " + str(self.strength) + " strength with " + str(
                    self.strength_bonus) + " bonus points " + " to strength")
