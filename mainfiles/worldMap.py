import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

# ---Player setup---


class Player:
    def __init__(self, name):
        self.name = name
        self.location = 'b2'
hero = Player('Tayotoka')


ZONENAME = '',
DESCRIPTION = 'description',
EXAMINATION = 'examine',
SOLVED = False,
UP = 'up',
DOWN = 'down',
LEFT = 'left',
RIGHT = 'right', 'east'

# Game functionality


def printLocation():
    """
    takes current player location
    prints out players location
    """
    print('\n' + ('#' * (4 + len(hero.location))))
    print(f'# {hero.location.upper()} #')
    print(f'# {zoneMap[hero.location][DESCRIPTION]} #')
    print('\n' + ('#' * (4 + len(hero.location))))


def prompt():
    """
    asks a question
    outputs players response
    """
    print('What would you like to do?')
    action = input().lower()
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit',
                          'examine', 'inspect', 'explore', 'shop']
    while action not in acceptable_actions:
        print(f'{action} is not a valid input, please try again: \n')
        action = input().lower()
    if action == 'quit':
        exit('Thank you for playing!')
    elif action == 'shop':
        shop()
    elif action in ['move', 'go', 'travel', 'walk']:
        playerMove(action)
    elif action in ['examine', 'inspect']:
        playerExamine(action)


def playerMove(action):
    """
    takes input on action, asks direction,
    outputs desired destination
    """
    ask = 'Where would you like to move to?\n'
    destination = input(ask)
    if destination in ['up', 'north']:
        destination = zoneMap[hero.location][UP]
        movementHandler(destination)
    elif destination in ['down', 'south']:
        destination = zoneMap[hero.location][DOWN]
        movementHandler(destination)
    elif destination in ['left', 'west']:
        destination = zoneMap[hero.location][LEFT]
        movementHandler(destination)
    elif destination in ['right', 'east']:
        destination = zoneMap[hero.location][RIGHT]
        movementHandler(destination)


def movementHandler(destination):
    """
    takes where player wants to go,
    moves player to location
    """
    print(f'You have moved to {destination}!')
    hero.location = destination
    printLocation()


def playerExamine(action):
    """
    takes information on items, creatures, ect,
    returns and prints information
    """
    pass

"""
------ Map ------ player starts at b2


-----------------
|   |   |   |   | a1  a2  a3  a4
 ----------------
|   |   |   |   | b1  b2  b3  b4
-----------------
|   |   |   |   | c1  c2  c3  c4
-----------------
|   |   |   |   | d1  d2  d3  d4
-----------------

"""

zoneMap = {
    'a1': {
        ZONENAME: 'Town',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: 'Forest - 1',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'a3': {
        ZONENAME: 'Forest - 2',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'a4': {
        ZONENAME: 'Forest - 3',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'b1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'description',
        EXAMINATION: 'A small house, no different then last time you saw it.',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'b4': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'c1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'c2': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'c3': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'c4': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'd1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'd2': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'd3': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'd4': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
}
prompt()
