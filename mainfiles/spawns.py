"""
This module will define all mob mechanics
"""
import pandas as pd
import itertools
import random
from fight import battle


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
        atkChance = random.randint(0, 8)
        if self.acc > other.eva - atkChance:
            other.hp -= (self.atk - other.defence)
        else:
            print('Your attack missed!')


def mobSpawn(lvl):
    if lvl <= 4:
        chance = random.randint(0, 21)
        if chance != 20:
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
for i in importedCreatures[0:4]:
    lowLvlMobs.append(Mob(*i))
for i in importedCreatures[4:6]:
    lowBoss.append(Mob(*i))

if __name__ == '__main__':
    mobSpawn()
