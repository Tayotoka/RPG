"""This module creates, shows, and handles items and container made objects"""
import sys
import time
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

    def __initBackpack__(self, rucksack, item_quantity = 0): 
        '''initializes the container backpack with items, once shop is integrated, arguments 
        will be passed in here to add to back pack. Note that the items added to ruck sack must
         be added everytime this method is called in test.'''
        
        # for i, j in rucksack:
            # print(f'this rucksack passed into initBackpack; defined by global scope {j.name, j.value, j.quantity}')
        # gold = item('Gold Coin', 1, 50)
        # sword = item('bronze sword', 50, 1)
        # potion = item('potion', 20, 1)
        # rucksack.add(sword)
        # rucksack.add(gold)
        # rucksack.add(potion)
        #items = []
        rucksack = rucksack.purchase(rucksack, gold, sword, potion)
        print(f'im out  of purchase, here is backpack {rucksack}')
        # x = rucksack.item_index(rucksack, potion.name)
        # print(f'this is value x {x}')
        rucksack.display_Backpack(self, rucksack, gold, sword, potion)
        return rucksack

    
    def display_Backpack(self, name, rucksack,*items):
        '''displays container backpacks contents'''

        print("\nThis is your backpack's contents.\n")
        count = 0
        #print(f'this is potion value = {items[2].value}')
        for name, item in rucksack:
            inbpack = f'{item.name}, x,{item.quantity},  - , {item.value} \n'
            for writetime in inbpack:
                sys.stdout.write(writetime)
                sys.stdout.flush()
                time.sleep(0.03)
            count += 1
        if count == 0:
            print('You have nothing in the backpack')
            #del self   #deleting used memory for testing purposes
        del count
        

    def item_index(self, rucksack, answer, num = 0):
        '''creates an inventory dictionary inv {keyvalue = item name and value = item value} 
        and unpacks the backpack container being sent as rucksack in this method. Takes user 
        input item name when called to request the value of the item from the backpack container.
        '''
        inv = {}
        inv2 = {}
        inventory = []
        for i, j in rucksack:
            inv[j.name] = j.value
            inv2[j.name] = j.quantity
        # print(inv)
        # print(inv2)
        inventory = [inv, inv2]
        # invent = f'\nthis is inventory {inventory}\n'
        # for writetime in invent:
        #     sys.stdout.write(writetime)
        #     sys.stdout.flush()
        #     time.sleep(0.03)
        return inventory[num][answer]

    def purchase(self, backpack, *items):
            print(f'\nim in purchase, here is backpack {backpack}\n')
            return backpack
#global created objects to manipulate in module backpack
backpack = container('Inventory')
gold = item('Gold Coin', 1, 50)
sword = item('bronze sword', 50, 1)
potion = item('potion', 20, 1)
backpack.add(sword)
backpack.add(gold)
backpack.add(potion)           
def test(answer = 'none'):
    '''creates backpack, intializes it, an communicates with other methods to 
    accept user input to request any status effects to activate upon item use
    '''
    print("Testing")

    global backpack

    backpack = backpack.__initBackpack__(backpack)
    
    if answer == 'none':
        while True:
            option = "Do you wish to use an item? Yes or No?\n"
            for writetime in option:
                sys.stdout.write(writetime)
                sys.stdout.flush()
                time.sleep(0.03)
            ask = input()
            if ask == "yes":
                answer = "i"
                break
            elif ask == "no":
                break
            else:
                prompt = "\nType in yes or no.\n"
                for writetime in prompt:
                    sys.stdout.write(writetime)
                    sys.stdout.flush()
                    time.sleep(0.03)
                
            

    if answer == 'i':
        #feed back loop for incorrect user input; if input is correct,
        #then item value for potion is unpacked when item index method is called from container class
        #and sent to variable ivalue and returned to attack method in character module
        while True:
            prompt = "\nChoose an item you want to use. You may also type in 'exit' or 'quit' to escape the inventory menu\n"
            for writetime in prompt:
                sys.stdout.write(writetime)
                sys.stdout.flush()
                time.sleep(0.03)
            ans = input().lower()
            if ans == 'potion':
                
                item_value = backpack.item_index(backpack, ans)
                decision = f'You chose support item {ans}.\n'
                for writetime in decision:
                    sys.stdout.write(writetime)
                    sys.stdout.flush()
                    time.sleep(0.03)
                potion_quantity = backpack.item_index(backpack, ans, 1)
                #print(f'i am potion quantity before use {potion_quantity}')
                
                if potion_quantity > 0:
                    
                    #print('im here')
                    for i, j in backpack:
                        print(f'Im in tuple {j.name}\n')
                        if j.name == 'potion':
                            #print(f'this is potion quantity before removal {j.quantity}')
                            j.quantity -= 1
                            #print(f'this is potion quantity after removal {j.quantity}')
                    # for i, j in backpack:
                    #         print(f'this is backpack after potion quantity removal{j.name, j.value, j.quantity}')
                    #potion quantity is decreased in test- success!
                else:
                    potion_quantity = 0 
                    item_value = 0
                    reminder = f'You have {potion_quantity} potions. \nYour hp has increased by {item_value}.\n'
                    for writetime in reminder:
                        sys.stdout.write(writetime)
                        sys.stdout.flush()
                        time.sleep(0.03)
                return item_value
            elif ans == 'exit' or ans == 'quit':
                break   
            else:
                warning = f'\nSorry, {answer} is not a support item.\n'
                for writetime in warning:
                    sys.stdout.write(writetime)
                    sys.stdout.flush()
                    time.sleep(0.03)
    else: 
        pass               
    #print(backpack.inside.items())
    

        # for item in items:
        #     if item.value > backpack[gold].quantity:
        #         print("You don't have enough gold!")
        #         print("""Come back when you have {0}
        #             more gold!""".format(item.value - backpack[gold].quantity))

        #     else:
        #         backpack.remove(gold, item.value)
        #         backpack.add(item)
        #         print('You purchased a {0}'.format(item.name))# text = input('quit?')
    # if text == 'yes':
    #     exit()

# if __name__ == '__main__':
#     print("im in statement")
#     test()