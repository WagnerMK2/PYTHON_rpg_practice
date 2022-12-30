import random
# import main3
import time

def Roll_D20():
    x = random.randint(1,20)
    if x == 1:
        print(x)
        return "Crit_fail"
    if x == 2 or x < 9:
        print(x)
        return "Light_success"
    if x == 9 or x <= 17:
        print(x)
        return "average_roll"
    if x == 18 or x == 19:
        print(x)
        return "Good_luck"
    if x == 20:
        print(x)
        return "Crit_success"
    else:
        return "ERROR"


#need to use objects and classes for these items.
def Generate_gold_item(roll):
    ''' diff base roll gives diff gold amounts
    '''
    if roll == "Light_success":
        gold = random.randint(2, 10)
        print(gold + str(" gold"))
        return gold + str(" gold")
    #this may need an f string
    if roll == "average_roll":
        gold = random.randint(5-15)
        print(gold + " gold")
        return str(gold + " gold")

def Generatate_gold_pouch(roll):
    '''this generates the amount of gold if a bag of gold needs to be generated'''
    if roll == "Light_success":
        gold = random.randint(4,16)
        return gold + " " + "gold"
    if roll == "average_roll":
        gold = random.randint(10-24)
        return gold
    if roll == "Good_luck":
        gold = random.randint(20-35)
        return gold
    elif roll == "Crit_success":
        gold = random.randint(35-55)
        return gold


#dictionary = {key:value, Key:value}
roll_items = ["assdffd", "sfadas", "asdfasdfsd", "sfasdf" ,"ewrqqwer" , "asdfasfasfasdf"]
adv_items = {"bag of holding":1, "theifs tools":2, "book":7, "ink well":5, "gold coins":4, "turtle shell":3, "goblet":8, "parchment":10,"cloth":6,"lockpicks":3,"lantern":9}
#item:rarity out of 10, ten being common,
magic_items_list= {"magic 1":3, "magic 2":4, "magic 3":9,"magic 99":7,"magic 10":5}

#make a function for generating gold coins. put reference to function in the dictionart. then the function randoms the amount of gold and leaves the stirng.



def populate_bookshelf():
    '''
    this function populates a bookshelf based on a D20 roll
    :param roll:
    :return:
    '''
    inventory = []
    x = Roll_D20()
    print(x)
    if x == "Crit_fail":
        y = random.randint(1,3)
     #   print(y)
        if y == 1:
            print("empty")
            inventory.append("Empty")
            print(inventory)
            return inventory
        elif y == 2 or y == 3:
            print("BOOBYTRAPPED")
            inventory.append("Boobytrap")
            print(inventory)
            return inventory
    elif x == "Light_success":
#       2-3 items
        for x in range(random.randint(2,3)):
            inventory.append(random.choice(list(adv_items.keys())))
        print(inventory)
    elif x == "average_roll":
#        3 - 5 items
        for x in range(random.randint(3,5)):
            inventory.append(random.choice(list(adv_items.keys())))
        print(inventory)
    elif x == "Good_luck":
#        3 - 5 items plus chance for magic item
        for x in range(random.randint(3,5)):
            inventory.append(random.choice(list(adv_items.keys())))
#random chance 3 in 10 for magic item  random.randint(1,10); if less than 3 add random magic item. if 4 and over pass;        inventory.append()
        print(inventory)
    elif x == "Crit_success":
#        3 - 5 items
        for x in range(random.randint(3,5)):
            inventory.append(random.choice(list(adv_items.keys())))
        inventory.append(random.choice(list(magic_items_list.keys())))
        print(inventory)

while True:
    ticker = 0
    populate_bookshelf()
    time.sleep(4)
    ticker += 1
    if ticker == 300:
        break
