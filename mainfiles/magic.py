class Magic(object):
    """
    takes in an instance
    creates a Magic object and grants it methods
    """
    def __init__(self, name, element, damage, mp, effect):
        self.name = name
        self.element = element
        self.damage = damage
        self.mp = mp
        self.effect = effect

    def useMagic(self, other):
        """
        takes self/other stats
        applies effects based on set constraints
        """
        pass


class Summons(object):
    """
    takes an instance
    creates an object for summoning creatures
    """

    def __init__(self, name, types, element, hp, atk, acc, eva):
        self.name = name
        self.element = element
        self.hp = hp
        self.atk = atk
        self.acc = acc
        self.eva = eva

fire = [
    Magic('Flare', 'Fire', 5, 5, 'Burn lvl1'),
    Magic('Enchant Weapon', 'Fire', None, 4, True)
]
# Enchant weapon adds additional damage to your weapon
water = [
    Magic('Water Whip', 'Water', 4, 3, -2),  # decreased eva
    Magic('Enchant Weapon', 'Water', None, 4, True)
]
wind = [
    Magic('Wind Blade', 'Wind', 3, 3, -1),  # decreases acc
    Magic('Enchant Weapon', 'Wind', None, 4, True)
]
earth = [
    Magic('Stone Fist', 'Earth', 3, 4, 'Stun lvl1'),
    Magic('Enchant Weapon', 'Earth', None, 4, True)
]
darkness = [
    Magic('Parvus Gravitas', 'Darkness', 2, 3, -4),
    Magic('Enchant Weapon', 'Darkness', None, 4, True)
]
ourSummon = [
    Summons('Atlas', 'Elemental', 'Fire', 10, 2, 2, 2),
]
