"""This module creates, shows, and handles items and container made objects"""
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

    def __initBackpack__(self, rucksack): 
        '''initializes the container backpack with items, once shop is integrated, arguments 
        will be passed in here to add to back pack'''
        gold = item('Gold Coin', 1, 50)
        sword = item('bronze sword', 50, 1)
        potion = item('potion', 20, 1)
        rucksack.add(sword)
        rucksack.add(gold)
        rucksack.add(potion)
        # x = rucksack.item_index(rucksack, potion.name)
        # print(f'this is value x {x}')
        rucksack.display_Backpack(self, rucksack, gold, sword, potion)
    
    def display_Backpack(self, name, rucksack,*items):
        '''displays container backpacks contents'''

        print("\nThis is your backpack's contents.\n")
        count = 0
        #print(f'this is potion value = {items[2].value}')
        for name, item in rucksack:
            print(item.name,' x', item.quantity, ' - ', item.value, '\n')
            count += 1
        if count == 0:
            print('You have nothing in the backpack')
            #del self   #deleting used memory for testing purposes
        del count

    def item_index(self, rucksack, answer):
        '''creates an inventory dictionary inv {keyvalue = item name and value = item value} 
        and unpacks the backpack container being sent as rucksack in this method. Takes user 
        input item name when called to request the value of the item from the backpack container.
        '''
        inv = {}
        
        for i, j in rucksack:
            inv[j.name] = j.value
        
        print(inv)
        return inv[answer]

def test(answer = 'none'):
    '''creates backpack, intializes it, an communicates with other methods to 
    accept user input to request any status effects to activate upon item use
    '''
    print("Testing")
    #creates backpack object instance out side of class scope and initalizes items in backpack
    backpack = container('Inventory')
    backpack.__initBackpack__(backpack)
    
    if answer == 'i':
        #feed back loop for incorrect user input; if input is correct,
        #then item value for potion is unpacked when item index method is called from container class
        #and sent to variable ivalue and returned to attack method in chracter module
        while True:
            print("\nChoose an item you want to use. You may also type in 'exit' or 'quit' to escape the inventory menu")
            ans = input().lower()
            if ans == 'potion':
                item_value = backpack.item_index(backpack, ans)
                print(f'You chose support item {ans}.')
                return item_value
            elif ans == 'exit' or ans == 'quit':
                break   
            else:
                print(f'\nSorry, {answer} is not a support item.')

    #print(backpack.inside.items())
    # def purchase(self, backpack, *items):

    #     for item in items:
    #         if item.value > backpack[gold].quantity:
    #             print("You don't have enough gold!")
    #             print("""Come back when you have {0}
    #                 more gold!""".format(item.value - backpack[gold].quantity))

    #         else:
    #             backpack.remove(gold, item.value)
    #             backpack.add(item)
    #             print('You purchased a {0}'.format(item.name))# text = input('quit?')
    # # if text == 'yes':
    # #     exit()

# if __name__ == '__main__':
#     print("im in statement")
#     test()