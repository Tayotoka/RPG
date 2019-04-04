"""
This module will define all mob mechanics
"""
import pandas as pd
import random
import sys
import time
import os
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
        self.status = []

    def attack(self, other):
        """
        takes in Mob and Player stats
        return new stats
        """
        theMobAttacks = f'\n{self.name} attacks...\n'
        for writetime in theMobAttacks:
                    sys.stdout.write(writetime)
                    sys.stdout.flush()
                    time.sleep(0.03)
        time.sleep(0.5)
        atkChance = random.randint(0, 7)
        if self.acc > other.eva - atkChance:
            other.hp -= (self.atk - other.defence)
        else:
            theMobMissed = f"The {self.name}'s attack missed!"
            for writetime in theMobMissed:
                sys.stdout.write(writetime)
                sys.stdout.flush()
                time.sleep(0.03)


def mobSpawn(lvl):
    """
    takes a list of creatures
    returns a random creature
    """
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
