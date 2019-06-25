import time
import sys
import os
# dialog functionality
wait03 = time.sleep(0.03)


# def outDialog(strings):
#     words = []
#     for s in len(strings):
#         words.append(s)
#         time.sleep(0.03)
#     return words

# story Dialog
gameStory = ['*You wake up groggy*', 'hello']

# npc general dialog
gameDialog = [
    'Hello!, welcome to this Text based RPG game!' + '\n' +
    'Use the Right and Left buttons to navigate text!',
    'You can view your character stats in "Character"' +
    '\n' + ' and Inventory in "BackPack"',
    '..',
    '...',
    '*rooster crows in the distance*'
]

# option dialog
