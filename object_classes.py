


class Item:
    def __init__(self, type, owner):
        '''this is where we should be creating the item. each item type created should have a ....

        '''
        self.name = #this should be passed back by the creation script
        self.type = {type}
        self.owner = {owner}
        #pull create type script from list. then it returns the name, specs and description


    def create(self,type,level,init_roll):
        '''creation doc string, this method creates the item with
        randomly varied specs based on level and what roll
        it was reated on.'''
        #{type} tells us what template to bring up
        #{level} tells up what range the stats are in
        #{init_roll} stat range modifier and special stat/effect chance


    def destroy(self):
        '''doc string, '''
        owner.inventory.remove(self)

class container:
    def __init__(self, type):
        ''' this is the init doc string'''
        self.condition = 1  # do i start this as a variable?
        self.inventory = populate_{type} #empty list, all containers start empty and have objects added.
        self.description = "words or variable go here" #each item should have at least a basic physical description

    def transfer(self,item,dest):
         '''this moves the item from this container to another container or player char'''
         if {item} in self.inventory():
             {dest}.append({item})
             self.inventory.remove({item})
             return "transfer completed"
         else:
             return "inventory_error"


