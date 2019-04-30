"""
this module defines all battle mechanics
"""
import time
import sys
import os


def battle(hero, newMob):
    """
    takes users input to decide battle sequence, does math for stats
    Returns stats
    """
    from character import Player  # these are here to only to circumvent
    from spawns import Mob        # circular dependency

    while hero.hp > 0 and newMob.hp > 0:
        # willRun = 'run'
        Player.attack(hero, newMob)

        mobTakesDmg = f'\n{newMob.name} now has {newMob.hp} hp left!'
        for writetime in mobTakesDmg:
            sys.stdout.write(writetime)
            sys.stdout.flush()
            time.sleep(0.01)

        if newMob.hp <= 0:
            break

        Mob.attack(newMob, hero)

        youTakeDmg = f'\n{newMob.name} attacked, you have {hero.hp} hp left!'
        for writetime in youTakeDmg:
            sys.stdout.write(writetime)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(0.5)
        os.system('cls')

if __name__ == '__main__':
    from character import Player
    battle(hero, newMob)
