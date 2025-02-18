import dragon 
import random

class FireDragon(dragon.Dragon):
  def __init__(self, name, max_hp, f_shots):
    super().__init__(name, max_hp)
    self._fire_shots = f_shots

  def special_attack(self, hero):
    if self._fire_shots > 0:
      damage = random.randint(5, 9)
      hero.take_damage(damage)
      self._fire_shots -= 1
      return f"{self.name} engulfs you in flames for {damage} damage!"
    else:
      return f"{self.name} attempts to engulf you in flames, but fails!"

  def __str__(self):
    return super().__str__() + f"\nFire Shots remaining: {self._fire_shots}"
    