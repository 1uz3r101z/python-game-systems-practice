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
    background = "Combat Soldier"
    health += 50
    strength += 80
    intelligence += 80 
    medical += 40
    supplies -= 20 
    ammo +=50
    trust += 0
    morale += 0
    romance = 0

elif background_choice == "2":
    background = " Medic" 
    health += 60
    strength -= 50
    intelligence += 85
    medical += 50
    supplies += 0
    ammo -= 80 
    trust += 0
    morale += 0
    romance = 0

elif background_choice == "3":
    background = "Engineer"
    health -= 20
    strength += 0
    intelligence += 90
    medical += 0
    supplies += 57
    ammo += 45
    trust += 0
    morale += 0
    romance = 0
else:
    background = " survivor" 
    health -= 50
    strength -= 46 
    intelligence -= 38
    medical += 0
    supplies += 0
    ammo -= 85
    trust += 0
    morale += 0
    romance = 0

print(f"\nWelcome {name} the {background}.")
print("You and your group have reached the final night of the outbreak.")

#--------------------------------------------------
#        COMPANION SELECTION
#--------------------------------------------------

print("\nChoose the companion closest to you:")
print("1. Maya - A fearless combat soldier")
print("2. Alex - A skilled engineer")
print("3. Jordan - A compassionate medic")

companion_choice = input("Enter 1, 2, or 3: ").strip()
if companion_choice == "1":
    companion = "Maya"
    companion_skill = "combat soldier"
elif companion_choice =="2":
    companion = "Alex"
    companion_skill = "engineer"

    
    
