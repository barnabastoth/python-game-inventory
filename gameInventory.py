# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

# Displays the inventory.

import csv
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def display_inventory(inventory):
    print("Inventory:")
    for k, v in inventory.items():
        print(v, k)
    print("Total number of items: " + str(sum(inventory.values())) +"\n")

# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inv[i] +=1
        else:
            inv.update({i:1})

# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    b = max(len(x) for x in inventory)
    qwe =[]
    for i in inv:
        qwe.append(inv[i])
    c = len(str(max(qwe)))
    count = "count"
    print("Inventory:" + "\n" + " " * c + "count:" + " " * b + "Item name:" +"\n" + "-"*(b+c+1))
    if order == "count,desc":
        a = sorted(inv, key=inv.get, reverse=True)
        for i in a:
            placeholder = ' {count:>{0}} {item:>' + str(b*2) + '}'
            print(placeholder.format(str(c*3),count=str(inv[i]), item=i))
    elif order == "count,asc":
        a = sorted(inv, key=inv.get)
        for i in a:
            print(str(inv[i]) + " " + i)
    elif None:
        pass
    else:
        pass
display_inventory(inv)
add_to_inventory(inv, dragon_loot)
display_inventory(inv)
print_table(inv, "count,desc")


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="test_inventory.csv"):
    with open('test_inventory.csv') as f:
         lines = [line.rstrip('   ') for line in f]
    print(lines)



import_inventory(inv)
# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    pass
