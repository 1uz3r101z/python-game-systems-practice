# THIS IS JUST A PRACTICE SCENARIO SO I CAN LEARN A THING OR TWO

print("xo" * 10)
print("    THE LAST NIGHT: Z0M813 APOCALYPSE  ")

#-------------------------------------------------------------
#                 CHARACTER CREATION
#-------------------------------------------------------------
name = input("n\Before the game begins tell me your name ")

name = input("Enter your name: ").strip() 

if name =="":
    name = "Player"
    
print("\nChoose your background:")
print("1. Soldier      - Srong in combat")
print("2. Medic        - Better at healing and using the cure")
print("3. Engineer     - Better at repairing and defending")
print("4. Survivor     - Balanced skills and extra supplies")

background_choice = input( " Enter 1, 2, 3 or 4: ").strip()

health = 100
strength = 100 
intelligence = 100 
medical = 50 
supplies = 50
ammo = 175  
trust = 60
morale = 75 
romance = 0 

if background_choice == "1":
    background = "Soldier"
    health += 
    strength += 80
    intelligence += 
    medical +=
    supplies +=
    ammo +=
    trust +=
    morale +=
    romance =

elif background_choice == "2":
    background = " Medic" 
    health +=
    strength +=
    intelligence +=
    medical +=
    supplies +=
    ammo +=
    trust +=
    morale +=
    romance =

elif background_choice == "3":
    background = "Engineer"
    health +=
    strength +=
    intelligence +=
    medical +=
    supplies +=
    ammo +=
    trust +=
    morale +=
    romance = 
else:
    background = " survivor" 
    health +=
    strength += 
    intelligence +=
    medical +=
    supplies +=
    ammo +=
    trust +=
    morale +=
    romance =

print(f"\nWelcome {name} the {background}.")
print("You and your group have reached the final night of the outbreak.")

#--------------------------------------------------
#        COMPANION SELECTION
#--------------------------------------------------
