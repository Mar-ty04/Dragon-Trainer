import entity
import random

class Hero(entity.Entity):
  def sword_attack(self, dragon):
    damage = random.randint(1, 6) + random.randint(1, 6)
    dragon.take_damage(damage)
    return f"You slash the {dragon.name} with your sword for {damage} damage!"

  def arrow_attack(self, dragon):
    damage = random.randint(1, 12)
    dragon.take_damage(damage)
    return f"You hit the {dragon.name} with an arrow for {damage} damage!"