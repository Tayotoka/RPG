"""This module creates, shows, and handles items and container made objects"""
import sys
import time
import os

print(__name__)
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

    def __initBackpack__(self, rucksack, hero, answer = "none"): 
        '''either sends user to shop and displays backpacks contents, or displays backpacks contents'''
        
        if answer == 'yes':
            rucksack = rucksack.purchase(hero, rucksack, gold, sword, potion)
    
        rucksack.display_Backpack(self, rucksack, gold, sword, potion)
        return rucksack

    
    def display_Backpack(self, name, rucksack,*items):
        '''displays container backpacks contents'''

        print("\nThis is your backpack's contents.\n")
        count = 0
        for name, item in rucksack:
            inbpack = f'{item.name}, x,{item.quantity},  - , {item.value} \n'
            for writetime in inbpack:
                sys.stdout.write(writetime)
                sys.stdout.flush()
                time.sleep(0.03)
            count += 1
        if count == 0:
            print('You have nothing in the backpack')
        #deleting used memory for testing purposes
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

        inventory = [inv, inv2]
        del inv, inv2
        return inventory[num][answer]
    def sendshopitems(self, hero):
        '''takes in players location to confirm shop location and sends a list of items when called 
        '''
        if hero.location == 'shop':
            return ["potion", "bronze sword"]
        else:
            pass
          
    def purchase(self, hero, backpack, *items ):
        '''when called the players username is used, the backpack and its contents is used to display shop items and ask user input for item purchase 
        and deducts necessary gold quantity after confirmation and restricts exceeding gold limit boundaries to purchase any more items and restricts
        any other item purchase requests other than shops stocked inventory. shop items are also sent here based on the players shop location.
        '''   
        stock = backpack.sendshopitems(hero)
        
        prompt = f'\n\nHello {hero.name}, welcome to the shop.\n\nHere is our items stocked in the shop:'
        for writetime in prompt:
            sys.stdout.write(writetime)
            sys.stdout.flush()
            time.sleep(0.03)
            
        for i in range(len(stock)):
            pmt = f'\n\n\t{stock[i]}\t\t10 gold\n\n'
            for writetime in pmt:
                sys.stdout.write(writetime)
                sys.stdout.flush()
                time.sleep(0.03)
        del stock
        while True:
            stock = backpack.sendshopitems(hero)
            ans = input("\n\nWould you like to purchase an item? yes or no?\n")
            os.system('cls')
            if ans == 'yes':
                prompt = f'\n\nHello {hero.name}, welcome to the shop.'
                for writetime in prompt:
                    sys.stdout.write(writetime)
                    sys.stdout.flush()
                    time.sleep(0.03)
                
                for i in range(len(stock)):
                    pmt = f'\n\n\t{stock[i]}\t10 gold\n\n'
                    for writetime in pmt:
                        sys.stdout.write(writetime)
                        sys.stdout.flush()
                        time.sleep(0.03)
                del stock
                ask = input("\n\nPlease type in the item name you would like to purchase.\n")
                os.system('cls')
                if ask == 'potion':
                    
                    for i, j in backpack:
                        if j.name == 'Gold Coin': 
                            if j.quantity >= 10:  

                                for i, j in backpack:
                                    if j.name == 'potion':

                                        j.quantity += 1
                                        prompt = f'Thank you for purchasing one {j.name}.'
                                        for writetime in prompt:
                                            sys.stdout.write(writetime)
                                            sys.stdout.flush()
                                            time.sleep(0.03)
                                        for k, l in backpack:
                                            if l.name == 'Gold Coin':
                                                l.quantity -= 10
                                                print(f'\nYou have {l.quantity} gold left.\n')
                                                backpack.display_Backpack(hero, backpack, potion, gold, sword)
                                                break                               
                            else:
                                warning = f'Sorry you do not have enough gold. You currently have {j.quantity} gold.'  
                                for writetime in warning:
                                    sys.stdout.write(writetime)
                                    sys.stdout.flush()
                                    time.sleep(0.03) 
                                continue    
                else:
                    print(f'\n\nsorry, {ask} is not in the shops inventory.')  
                    continue      
            elif ans == 'no':
                break
            else:
                print(f'\n\nsorry, {ans} is not a valid input.')
                continue
        
        return backpack
#global created objects to manipulate in module backpack
backpack = container('Inventory')
gold = item('Gold Coin', 1, 50)
sword = item('bronze sword', 50, 1)
potion = item('potion', 20, 1)
backpack.add(sword)
backpack.add(potion) 
backpack.add(gold)


def test(hero, answer = "none" ):
    '''reads global created objects and contains multiple calling options to either access the shop, or look at inventory 
    and request user input for item use in or out of attack phase
    '''
    print("Testing")

    global backpack
    #do i keep initbackpack or delete it to use purchase method?
    if answer == 'yes':
        backpack = backpack.__initBackpack__(backpack, hero, answer)

    if answer == "none":
        backpack.display_Backpack(hero, backpack, potion, gold, sword)
        while True:

            option = "Do you wish to use an item? Yes or No?\n"
            for writetime in option:
                sys.stdout.write(writetime)
                sys.stdout.flush()
                time.sleep(0.03)
            ask = input()
            os.system('cls')
            
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

            backpack.display_Backpack(hero, backpack, potion, sword, gold)
            prompt = "\nChoose an item you want to use. You may also type in 'exit' or 'quit' to escape the inventory menu\n"
            for writetime in prompt:
                sys.stdout.write(writetime)
                sys.stdout.flush()
                time.sleep(0.03)
            ans = input().lower()
            os.system('cls')

            if ans == 'potion':
                
                item_value = backpack.item_index(backpack, ans)
                
                decision = f'You chose support item {ans}.\n'
                for writetime in decision:
                    sys.stdout.write(writetime)
                    sys.stdout.flush()
                    time.sleep(0.03)
                potion_quantity = backpack.item_index(backpack, ans, 1)
                
                if potion_quantity > 0:
                
                    for i, j in backpack:
                        if j.name == 'potion':
                            j.quantity -= 1
                            update = f'\npotion x{j.quantity} - {j.value}.\n'
                            for writetime in update:
                                sys.stdout.write(writetime)
                                sys.stdout.flush()
                                time.sleep(0.03) 
                else:
                    potion_quantity = 0 
                    item_value = 0
                    reminder = f'You have {potion_quantity} potions.\n'
                    for writetime in reminder:
                        sys.stdout.write(writetime)
                        sys.stdout.flush()
                        time.sleep(0.03)
                return item_value
            elif ans == 'exit' or ans == 'quit':
                break   
            else:
                warning = f'\nSorry, {ans} is not a support item.\n'
                for writetime in warning:
                    sys.stdout.write(writetime)
                    sys.stdout.flush()
                    time.sleep(0.03)
    else: 
        pass               
print("\nread all")