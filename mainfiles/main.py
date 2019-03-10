"""
Text based RPG, battle random monsters.
"""
from charmob import player, mob, potion, battle
import random


def mainGame():

    """
    Main game application
    """
    monsters = [mob('Slime', [10, 3, 2]), mob('Goblin', [12, 4, 1]),
                mob('Earth Elemental', [15, 4, 2])]
    cont = 'y'  # start menu option
    game = 'y'  # game option

    while cont.lower() == 'y':
        print('welcome! what would you like to do?\n \nStart \nLoad \nQuit \n')

        options = input()

        if options.lower() == 'quit':
            exit('Thank you for playing!')
        elif options.lower() == 'load':
            print('Coming soon!')
        elif options.lower() == 'start':
            break
        else:
            print('\nYou entered an invalid option! Please Try again.\n')

    userName = input('\nWhat is your username?: ')

    hero = player(userName, 15, 10, [15, 5, 2], 50)
    # name, mainHp, mainMp, [hp, atk, def], money

    while True:

        print('\nPlease select the folowing:\n\nExplore \nShop \nQuit \n')

        newOptions = input()

        if newOptions.lower() == 'quit':
            exit('Have a nice day!')

        elif newOptions.lower() == 'shop':
            print('coming soon!')

        else:  # this is the battle loop starting point

            newMob = random.choice(monsters) # picks random monster

            print(f'\n{newMob.name} has appeared!!\n')

            battle(hero, newMob)  # Battle function

            if hero.stats[0] > 0:
                print(f'\nYou killed the {newMob.name}!!')

            else:
                print(f'You were killed by the {newMob.name}.')
                break

        monsters = [mob('Slime', [10, 3, 2]), mob('Goblin', [12, 4, 1]),
                    mob('Earth Elemental', [15, 4, 2])]


if __name__ == '__main__':
    mainGame()
