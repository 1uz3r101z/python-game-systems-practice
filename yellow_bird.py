#INVENTORY SYSTEM 

inventory = []

inventory.append("Silver Key")
inventory.append("Old Letter")

print("Inventory: ")
for item in inventory: 
    print("-", item)

# PRACTICE CHECKING FOR ITEMS

if "Silver Key" in inventory:
  print("You unlock the door.")
else: 
    print("The door is locked.")
