#Choice + Branching System

choice = input("Go to the library or roofttop?").lower()

if choice == "Library":
  print("You find a mysterious notebook.")
elif choice == "Rooftop":
  print("Someone is waiting for you.")
else:
  print("You stay where you are.")
  
