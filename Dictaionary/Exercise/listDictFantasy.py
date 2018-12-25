
def addToInventory(inventory, addedItems):
	for i in range (len(addedItems)) :
		inventory.setdefault(str(addedItems[i]),0)
		inventory[addedItems[i]] =  inventory[addedItems[i]] +1 
	return inventory
def displayInventory(inv):
	total = 0
	for i, j in inv.items():
		print(str(j) + ' ' + i)
		total += j
	print('Total number of items: ' + str(total))
inv = {'gold coin': 42, 'rope' :1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)


