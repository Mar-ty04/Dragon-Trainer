import dragon 
import random 

class FlyingDragon(dragon.Dragon):
  def __init__(self, name, max_hp, swoops):
    super().__init__(name, max_hp)
    self._swoops = swoops

  def special_attack(self, hero):
    if self._swoops > 0:
      damage = random.randint(5, 8)
      hero.take_damage(damage)
      self._swoops -= 1
      return f"{self.name} swoops down and knocks you over for {damage} damage!"
    else:
      return f'{self.name} attempts to swoop down and knock you over but fails!'

  def __str__(self):
    return super().__str__() + f"\nSwoop attacks remaining: {self._swoops}"