"""
this module defines all battle mechanics
"""


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

        print(f'\n{newMob.name} now has {newMob.hp} hp left!')

        if newMob.hp <= 0:
            break

        Mob.attack(newMob, hero)

        print(f'\n{newMob.name} attacked, you have {hero.hp} hp left!')

if __name__ == '__main__':
    battle()
