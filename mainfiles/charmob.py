"""
player, mobs, npc, and general function for text based RPG
"""
import pandas as pd
from backpack import item, container, purchase
import itertools
import random


class Player(object):
    """
    Takes player instance, creates player methods
    """
    def __init__(self, name, level, mainHp, mainMp,
                 hp, mp, atk, defence, acc, eva, weight, money, exp):
        self.name = name
        self.level = level
        self.mainHp = mainHp
        self.mainMp = mainMp
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.defence = defence
        self.acc = acc
        self.eva = eva
        self.weight = weight
        self.money = money
        self.exp = exp

    def attack(self, other):
        """
        takes player stats and targets stats
        minuses def from attack and outputs correct parameters
        """
        answer = input('What would you like to do? \n\nAttack \nItem \n')
        if answer.lower() == 'attack':
            other.hp -= (self.atk - other.defence)
        elif answer.lower() == 'item':
            print('Coming soon!')
            # print(f'Would you like to use your {hpPotion[0].name}? y/n\n')
            # usepotion = input()

            # if usepotion.lower() == 'y':
            #     self.useItem(hpPotion[0])
            # else:
            #     pass
        else:
            print('\nYou stumbled!\n')

    def NeededExp(self):
        """
        takes player exp/level,
        returns if player levels up
        """
        newlvl = expToLevel[self.level + 1]
        if self.exp >= newlvl:
            self.level += 1
            print(f'Congratulations! you reached Level {self.level}!')

        else:
            untilLevel = newlvl - self.exp
            print(f"""You need {untilLevel} Experience until level {self.level+1}!""")

# experience
df = pd.read_excel('Data/Experience.xlsx', sheet_name='None')

experience = df.values.tolist()  # the packed list
expToLevel = []  # the unpacked list
for e in experience:
    expToLevel.append((*e))  # unpacks list


class Mob(object):
    """
    takes monster stats and player stats
    minuses def from attack and outputs correct parameters
    """
    def __init__(self, name, types, level, hp, atk,
                 defence, acc, eva, tier, exp, gold):
        self.name = name
        self.level = level
        self.types = types
        self.hp = hp
        self.atk = atk
        self.defence = defence
        self.acc = acc
        self.eva = eva
        self.tier = tier
        self.exp = exp
        self.gold = gold

    def attack(self, other):
        print(f'\n{self.name} attacks...')
        other.hp -= (self.atk - other.defence)


def mobSpawn(lvl):
    if lvl <= 4:
        chance = random.randint(0, 11)
        if chance != 10:
            newMob = random.choice(lowLvlMobs)
            return newMob
        else:
            newMob = random.choice(lowBoss)
            return newMob
    else:
        print('No mobs for your level yet, sorry!')


# Creatures
df = pd.read_excel('Data/Creatures.xlsx', sheet_name='None')

importedCreatures = df.values.tolist()  # the packed list
creatures = []  # the unpacked list
lowLvlMobs = []
lowBoss = []
for i in importedCreatures:
    creatures.append(Mob(*i))  # unpacks list
for i in importedCreatures[0:5]:
    lowLvlMobs.append(Mob(*i))
for i in importedCreatures[5:6]:
    lowBoss.append(Mob(*i))


def battle(hero, newMob):
    """
    takes users input to decide battle sequence, does math for stats
    Returns stats
    """
    while hero.hp > 0 and newMob.hp > 0:
        Player.attack(hero, newMob)

        print(f'\n{newMob.name} now has {newMob.hp} hp left!')

        if newMob.hp <= 0:
            break

        Mob.attack(newMob, hero)

        print(f'\n{newMob.name} attacked, you have {hero.hp} hp left!')


class Potion(Player):

    def __init__(self, name, types, effects, value, weight):
        self.name = name
        self.types = types
        self.effects = effects
        self.value = value
        self.weight = weight

    def useItem(self, other):
        """
        takes a potion object and player object stats
        outputs renewed player stats
        """
        print(""" What would you like to use?
              1: Health Potion
              2: Mana Potion
              3: --Coming soon--""")

        myItem = 'Enter a number for the item you want to use.'

        if myItem == '1':
            pass
        elif myItem == '2':
            pass
        elif myItem == '3':
            print('New Options coming soon!')
        else:
            print('Sorry, thats not a valid input.')

# Potions
df = pd.read_excel('Data/potions.xlsx', sheet_name='None')

importedPotions = df.values.tolist()  # the packed list
potions = []                          # the unpacked list
hpPotions = []
mpPotions = []
for p in importedPotions:
    potions.append(Potion(*p))

for p in importedPotions[0:3]:
    hpPotions.append(Potion(*p))      # unpacks list to hp

for p in importedPotions[3:6]:
    mpPotions.append(Potion(*p))      # unpacks list to mp
