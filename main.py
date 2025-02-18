#Marisol Morales & Andreas Moreno, 3/5/2024, Lab 6 Dragon Trainer
from hero import Hero 
from dragon import Dragon
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
import check_input
import random

def main():
  print('What is your name, challenger?')
  player_name = input()
  print(f'Welcome to dragon training, {player_name}')
  print('You must defeat 3 dragons.')
  print()
  hero = Hero(player_name, 50)
  dragons = [Dragon('Deadly Nadder', 10), FireDragon('Gronckle', 15, 3), FlyingDragon('Timberjack', 20, 5)]
  
  while hero.hp > 0 and len(dragons) > 0:
    print(hero)
    for i, dragon in enumerate(dragons):
      print(f'{i + 1}. {dragon}')
    pick_dragon = check_input.get_int_range('Choose a dragon to attack: ', 1, len(dragons))
    print()

    print("Attack with:")
    print("1. Arrow (1 D12)")
    print("2. Sword (2 D6)")

    attack_type = check_input.get_int_range('Enter weapon: ', 1, 2)
    print()
    if attack_type == 1:
      print(hero.arrow_attack(dragons[pick_dragon - 1]))
      print()
    if attack_type == 2:
      print(hero.sword_attack(dragons[pick_dragon - 1]))
      print()

    if dragons[pick_dragon-1].hp <= 0:
      dragons.remove(dragons[pick_dragon-1])
      
    if len(dragons) > 0:
      dragon_attack = random.choice(dragons)
      dragon_attack_type = random.randint(1, 2)
      if dragon_attack_type == 1:
        print(dragon_attack.basic_attack(hero))
        print()
      if dragon_attack_type == 2:
        print(dragon_attack.special_attack(hero))
        print()

  if hero.hp <= 0:
    print('You have been defeated.')
  else:
    print('Congratulations! You have defeated all 3 dragons, you have passed the trials.')
    
main()