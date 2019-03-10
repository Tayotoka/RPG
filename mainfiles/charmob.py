"""
player, mobs, npc, and general function for text based RPG
"""


class player(object):
    """
    Takes player instance, creates player methods
    """
    def __init__(self, name, mainHp, mainMp, stats, money):
        self.name = name
        self.stats = stats
        self.money = money
        self.mainHp = mainHp
        self.mainMp = mainMp

    def attack(self, other):
        """
        takes player stats and targets stats
        minuses def from attack and outputs correct parameters
        """
        answer = input('What would you like to do? \n\nAttack \nItem \n')
        if answer.lower() == 'attack':
            other.stats[0] -= (self.stats[1] - other.stats[2])
        elif answer.lower() == 'item':
            print(f'Would you like to use your {hpPotion[0].name}? y/n\n')
            usepotion = input()

            if usepotion.lower() == 'y':
                self.useItem(hpPotion[0])
            else:
                pass
        else:
            print('\nYou stumbled!\n')

    def useItem(self, other):
        """
        takes a potion object and player object stats
        outputs renewed player stats
        """
        if self.stats[0] < self.mainHp:

            self.stats[0] += hpPotion[0].effects

            if self.stats[0] > self.mainHp:

                self.stats[0] = self.mainHp

            print(f'{self.name} has healed and now has {self.stats[0]} HP!')
        else:
            print('Your health is already at max HP!!')


class mob(object):
    """
    takes monster stats and player stats
    minuses def from attack and outputs correct parameters
    """
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def attack(self, other):
        print(f'\n{self.name} attacks...')
        other.stats[0] -= (self.stats[1] - other.stats[2])


def battle(hero, newMob):
    """
    takes users input to decide battle sequence, does math for stats
    Returns stats
    """
    while hero.stats[0] > 0 and newMob.stats[0] > 0:
        player.attack(hero, newMob)

        print(f'\n{newMob.name} now has {newMob.stats[0]} hp left!')

        if newMob.stats[0] <= 0:
            break

        mob.attack(newMob, hero)

        print(f'\n{newMob.name} attacked, you have {hero.stats[0]} hp left!')


class potion(object):
    """
    creates instances of potions
    """
    def __init__(self, name, types, effects):

        self.name = name
        self.types = types
        self.effects = effects

hpPotion = [potion('Crude Health Potion', 'hp_Potion', 10),
            potion('Basic Health Potion', 'hp_Potion', 25)]
