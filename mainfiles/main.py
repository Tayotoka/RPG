"""
Text based RPG, battle random monsters.
"""
import random
import sys
import os
import time
from character import Player, zoneMap
from spawns import (Mob, creatures, mobSpawn)
from fight import battle
import backpack
import worldMap

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
        elif startQuestion == 'load':
            loadGame()
        elif startQuestion == 'help':
            getHelp()
        elif startQuestion == 'options':
            options()
        elif startQuestion == 'quit':
            exit('Thank you for playing!')
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
    whatsUser = '\nWhat is your username?: '
    for writetime in whatsUser:
        sys.stdout.write(writetime)
        sys.stdout.flush()
        time.sleep(0.03)
    userName = input()
    hero = Player(userName, 1, 15, 10, 15, 10, 5, 2, 3, 3, 10, 50, 0)
    # name, level, mainHp, mainMp, hp, atk, def, acc, eva, weight, exp, money
    os.system('cls')
    welcomeText = f'\nWelcome {hero.name}!\n'

    for writetime in welcomeText:
        sys.stdout.write(writetime)
        sys.stdout.flush()
        time.sleep(0.03)
    gameStart(hero)
ZONENAME = '',
DESCRIPTION = 'description',
EXAMINATION = 'examine',
SOLVED = False,
UP = 'up',
DOWN = 'down',
LEFT = 'left',
RIGHT = 'right', 'east'

def playerExamine(action):
    """
    takes information on items, creatures, ect,
    returns and prints information
    """
    pass
    
def prompt(hero):
        """
        takes users input
        outputs players response
        """
        action = input().lower()
        os.system('cls')
        acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit',
                              'examine', 'inspect', 'explore', 'shop', 'inventory']
        while action not in acceptable_actions:
            print(f'{action} is not a valid input, please try again: \n')
            action = input().lower()
        if action == 'quit':
            exit('Thank you for playing!')
        elif action == 'inventory':
            
            ivalue = backpack.test(hero)
            if ivalue:
                hero.hp += ivalue
                stat_up = f'\n{hero.name}s hp increased by {ivalue}.'
                for writetime in stat_up:
                    sys.stdout.write(writetime)
                    sys.stdout.flush()
                    time.sleep(0.03)
                del ivalue
            else:
                del ivalue
        elif action == 'shop':
            
            print(hero.location)
            
            data = worldMap.retrieve_wmdata(hero.location)
            if data == 'Shop':
                backpack.test(hero,'yes')
            else:
                prompt = f'Please head to your nearest shop location to request the shop option.'
                for writetime in prompt:
                    sys.stdout.write(writetime)
                    sys.stdout.flush()
                    time.sleep(0.03)

        elif action in ['move', 'go', 'travel', 'walk']:
            print(hero.location)
            Player.playerMove(hero, action)

        elif action in ['examine', 'inspect']:
            playerExamine(action)

        elif action in 'explore':
            explore(hero)


def printLocation(hero):
    """
    takes current player location
    prints out players location
    """
    print('\n' + ('#' * (4 + len(hero.location))))
    print(f'# {hero.location.upper()} #')
    print(f'# {zoneMap[hero.location][DESCRIPTION]} #')
    print('#' * (4 + len(hero.location)))
    prompt(hero)


def explore(hero):
    newMob = mobSpawn(hero.level)

    os.system('cls')
    mobAppears = f'\n{newMob.name} has appeared!!\n'
    for writetime in mobAppears:
        sys.stdout.write(writetime)
        sys.stdout.flush()
        time.sleep(0.02)

    battle(hero, newMob)  # Battle function

    if hero.hp and newMob.hp > 0:
        print('Got away safely!')

    elif hero.hp > 0:
        os.system('cls')
        youWon = f'\nYou killed the {newMob.name}!!\n'
        for writetime in youWon:
            sys.stdout.write(writetime)
            sys.stdout.flush()
            time.sleep(0.03)

        hero.exp += newMob.exp
        hero.NeededExp()
        time.sleep(1.5)
        os.system('cls')
        #mainUI(hero)
    else:
        os.system('cls')
        youDied = f'\nYou were killed by the {newMob.name}.\n'
        for writetime in youDied:
            sys.stdout.write(writetime)
            sys.stdout.flush()
            time.sleep(0.04)
            time.sleep(1)
        os.system('cls')
        #mainUI(hero)

def mainUI(hero):
    """
    takes in hero
    prints out main options
    """
    gamemech = """\nPlease select the following:
                      \nMove \nExplore \nShop \nInventory \nQuit\n"""

    for writetime in gamemech:
        sys.stdout.write(writetime)
        sys.stdout.flush()
        time.sleep(0.02)


def gameStart(hero):
    """
    takes inputs from modules and player,
    outputs actual game content.
    """
    while True:
        mainUI(hero)
        # newOptions = input()
        prompt(hero)
    # this is the battle loop starting point

if __name__ == '__main__':
    print(__name__)
    startScreen()
    
