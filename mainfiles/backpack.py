class item(object):
    def __init__(self, name, value, quantity=1):
        self.name = name
        self.raw = name.strip().lower()
        self.quantity = quantity

        self.value = value
        self.netValue = quantity * value

    def recalc(self):
        self.netValue = self.quantity * self.value


class container(object):

    def __init__(self, name):
        self.name = name
        self.inside = {}

    def __iter__(self):
        return iter(self.inside.items())

    def __len__(self):
        return len(self.inside)  # length of inside

    def __contains__(self, item):  # checks if in inventory
        return item.raw in self.inside

    def __getitem__(self, item):
        return self.inside[item.raw]
        # this allows us to call an item by its name

    def __setitem__(self, item, value):
        self.inside[item.raw] = value
        return self[item]

    def add(self, item, quantity=1):

        if quantity < 0:
            raise ValueError('Negative quantity.')  # can use remove() instead

        if item in self:

            self[item].quantity += quantity  # adds to quantity
            self[item].recalc()

        else:
            self[item] = item  # if no item, just add it

    def remove(self, item, quantity=1):

        if item not in self:
            raise KeyError('Item not in container')
        if quantity < 0:
            raise ValueError('Negative quantity.')  # same as earlier

        if self[item].quantity <= quantity:
            del self.inside[item.raw]

        else:
            self[item].quantity -= quantity
            self[item].recalc()

backpack = container('Inventory')

sword = item('Sword', 10)
gold = item('Gold Coin', 1, 50)
potion = item('potion', 5)

backpack.add(sword)
backpack.add(gold)


# print(sword in backpack)
# print(gold in backpack)
# print(potion in backpack)

# print(len(backpack))

# for name, item in backpack:
#     print(item.name, item.quantity)


def purchase(*items):

    for item in items:
        if item.value > backpack[gold].quantity:
            print("You don't have enough gold!")
            print("""Come back when you have {0}
                  more gold!""".format(item.value - backpack[gold].quantity))

        else:
            backpack.remove(gold, item.value)
            backpack.add(item)
            print('You purchased a {0}'.format(item.name))

print(backpack[gold].quantity)

purchase(sword, sword, potion, potion)

print(backpack[gold].quantity)

print(len(backpack))
