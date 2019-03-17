"""
Text based RPG, battle random monsters.
"""
import random
from character import Player
from spawns import (Mob, creatures, mobSpawn)
from fight import battle


def mainGame():

    """
    Main game application
    """
    while True:
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
    hero = Player(userName, 1, 15, 10, 15, 10, 5, 2, 3, 3, 10, 50, 0)
    # name, mainHp, mainMp, hp, atk, def, acc, eva, weight, exp, money
    print(f'\nWelcome {hero.name}!\n')

    while True:

        print('\nPlease select the folowing:\n\nExplore \nShop \nQuit')

        newOptions = input()

        if newOptions.lower() == 'quit':
            exit('Have a nice day!')

        elif newOptions.lower() == 'shop':
            print('coming soon!')

        else:  # this is the battle loop starting point

            newMob = mobSpawn(hero.level)

            print(f'\n{newMob.name} has appeared!!\n')

            battle(hero, newMob)  # Battle function

            if hero.hp and newMob.hp > 0:
                print('Got away safely!')

            elif hero.hp > 0:
                print(f'\nYou killed the {newMob.name}!!\n')
                hero.exp += newMob.exp
                hero.NeededExp()

            else:
                print(f'\nYou were killed by the {newMob.name}.\n')
                break


if __name__ == '__main__':
    mainGame()
