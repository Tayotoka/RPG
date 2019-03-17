"""
This module dictates character development.
"""
import pandas as pd
import itertools
import random
from fight import battle


class Player(object):
    """
    Takes player instance, creates player methods
    """
    def __init__(self, name, level, mainHp, mainMp,
                 hp, mp, atk, defence, acc, eva, weight, gold, exp):
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
        self.gold = gold
        self.exp = exp

    def attack(self, other):
        """
        takes player stats and targets stats
        minuses def from attack and outputs correct parameters
        """
        answer = input('What would you like to do? \n\nAttack \nItem,\nRun \n')
        if answer.lower() == 'attack':
            atkChance = random.randint(0, 8)
            if self.acc > other.eva - atkChance:
                other.hp -= (self.atk - other.defence)
            else:
                print('Your attack missed!')
        elif answer.lower() == 'item':
            print('Coming soon!')
            # print(f'Would you like to use your {hpPotion[0].name}? y/n\n')
            # usepotion = input()

            # if usepotion.lower() == 'y':
            #     self.useItem(hpPotion[0])
            # else:
            #     pass
        elif answer.lower() == 'run':
            print('Sorry, coming soon!')
        # elif answer.lower() == 'run':
        #     runChance = random.randint(0, 11)
        #     if runChance >= 8:
        #         return 'run'
        #     else:
        #         print("\nYou couldn't escape!\n")
        else:
            print('\nYou stumbled!\n')

    def levelUp(self):
        self.mainHp += 3
        self.mainMp += 2
        self.hp += 3
        self.mp += 2
        self.atk += 2
        self.defence += 1
        self.acc += 1
        self.eva += 1

    def NeededExp(self):
        """
        takes player exp/level,
        returns if player levels up
        """
        newlvl = expToLevel[self.level + 1]
        if self.exp >= newlvl:
            self.level += 1
            self.levelUp()
            print(self.mainHp)
            print(f'Congratulations! you reached Level {self.level}!')

        else:
            untilLevel = newlvl - self.exp
            print(f"{untilLevel} Experience until level {self.level+1}!")

# experience
df = pd.read_excel('Data/Experience.xlsx', sheet_name='None')

experience = df.values.tolist()  # the packed list
expToLevel = []  # the unpacked list
for e in experience:
    expToLevel.append((*e))  # unpacks list
