# RELATIONSHIP/AFFECTION SYSTEM

affection = 0

choice = input("Compliment them? yes/no: ")

if choice == "yes":
    affection += 2
else:
  affection -= 1
print("Affection: ", affection)


if affection >=5:
  print("Special bonding scene unlocked!")
  
  
