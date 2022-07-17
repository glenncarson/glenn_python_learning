
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print "Inventory:"
    total_count = 0
    for item in inventory:
        print str(inventory[item]) + " {}".format(item)
        total_count += inventory[item]
    print "Total number of items: {}".format(str(total_count))

displayInventory(inventory)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] += 1
    return inventory
# try the setdefault method to update an existing dictionary, iteratively over a list
updated_inventory = addToInventory(inventory,dragonLoot)
# print updated_inventory
displayInventory(updated_inventory)