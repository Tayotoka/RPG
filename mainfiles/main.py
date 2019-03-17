"""
Text based RPG, battle random monsters.
"""
import random
import sys
import os
import time
from character import Player
from spawns import (Mob, creatures, mobSpawn)
from fight import battle


def startScreen():
    print('--------Welcome!-------\n')
    print('What would you like to do?\n')
    print('---------Start---------\n')
    print('---------Load----------\n')
    print('---------Help----------\n')
    print('--------Options--------\n')
    print('---------Quit----------\n')
    while True:

        startQuestion = input().lower()

        if startQuestion == 'start':
            getName()
        elif startQuestion == 'help':
            getHelp()
        elif startQuestion == 'options':
            options()
        elif startQuestion == 'quit':
            exit('Thank you for playing!')
        elif startQuestion == 'load':
            loadGame()
        else:
            print(f'Sorry, {startQuestion} is not a valid input!')


def getHelp():
    """
    displays things that can be done.
    """
    pass


def options():
    """
    explains different options for the game.
    """
    pass


def loadGame():
    """
    takes input on what player character to load,
    returns desired game instance.
    """
    pass


def getName():
    """
    takes players name,
    returns player as a class object.
    """
    os.system('cls')
    userName = input('\nWhat is your username?: ')
    hero = Player(userName, 1, 15, 10, 15, 10, 5, 2, 3, 3, 10, 50, 0)
    # name, level, mainHp, mainMp, hp, atk, def, acc, eva, weight, exp, money
    os.system('cls')
    welcomeText = f'\nWelcome {hero.name}!\n'

    for writetime in welcomeText:
            sys.stdout.write(writetime)
            sys.stdout.flush()
            time.sleep(0.03)
    gameStart(hero)


def gameStart(hero):
    """
    takes inputs from modules and player,
    outputs actual game content.
    """
    while True:

        gamemech = '\nPlease select the folowing:\n\nExplore \nShop \nQuit\n'

        for writetime in gamemech:
            sys.stdout.write(writetime)
            sys.stdout.flush()
            time.sleep(0.04)

        newOptions = input()

        if newOptions.lower() == 'quit':
            exit('Have a nice day!')

        elif newOptions.lower() == 'shop':
            print('coming soon!')

        else:  # this is the battle loop starting point

            newMob = mobSpawn(hero.level)

            os.system('cls')
            mobAppears = f'\n{newMob.name} has appeared!!\n'
            for writetime in mobAppears:
                sys.stdout.write(writetime)
                sys.stdout.flush()
                time.sleep(0.04)

            battle(hero, newMob)  # Battle function

            if hero.hp and newMob.hp > 0:
                print('Got away safely!')

            elif hero.hp > 0:
                os.system('cls')
                youWon = f'\nYou killed the {newMob.name}!!\n'
                for writetime in youWon:
                    sys.stdout.write(writetime)
                    sys.stdout.flush()
                    time.sleep(0.04)

                hero.exp += newMob.exp
                hero.NeededExp()
                time.sleep(2)
                os.system('cls')
            else:
                os.system('cls')
                youDied = f'\nYou were killed by the {newMob.name}.\n'
                for writetime in youDied:
                    sys.stdout.write(writetime)
                    sys.stdout.flush()
                    time.sleep(0.04)
                    time.sleep(1)
                os.system('cls')
                break

if __name__ == '__main__':
    startScreen()
