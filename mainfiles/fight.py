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
    import backpack 
    
    while hero.hp > 0 and newMob.hp > 0:
            # willRun = 'run'
            #executes attack method from player class and stores in variable ivalue
        ivalue = Player.attack(hero, newMob)

            #if ivalue exists, then increase heros hp attribute and deletes ivalue after its been used
        if ivalue:
            #status effect implemented from support item
            hero.hp += ivalue
            del ivalue
        else:
            #deletes ivalue if not in existence
            del ivalue

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


def magic(hero, newMob):
    """
    takes character stats and magic
    outputs damage
    """
    from character import Player  # these are here to only to circumvent
    from spawns import Mob        # circular dependency
    whatMagic = 'What would you like to you?'
    for writetime in whatMagic:
        sys.stdout.write(writetime)
        sys.stdout.flush()
        time.sleep(0.01)
    for i in hero.magic:
        print(i)

# if __name__ == '__main__':
#     from character import Player
#     battle(hero, newMob)
