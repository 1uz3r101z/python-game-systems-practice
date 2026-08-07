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
    background = "combat soldier"
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
    background = "medic" 
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
    background = "engineer"
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
    background = "survivor" 
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
else: 
    companion = "Jordan"
    companion_skill = "medic"

print (f"\n{companion} has stayed beside you throughout the outbreak.")

#        IMPORTANT STORY VARIABLES

saved_friend = False
found_cure = False
cure_intact = False 
vehicle_working = False
base_defended = False
leader_alive = True 
companion_alive = True 
bitten = False
rescued_survivors = False

#-----------------------------------------------------------------
#               CHAPTER 1: THE SUPPLY RUN
#-----------------------------------------------------------------

print("xo" * 14)
print ("CHAPTER 1: THE ABANDONED PHARMACY")
print("xo" * 14)

print(
    "\nYour group is almost out of medicine."
    "A nearby pharmacy may contain valuable supplies..."
    "but the streets are filled with infected."
)

print ("\nWhat do you do?")
print("1. Search the Pharmacy carefully.")
print("2. Raid it qquickly before more zombies arrive.")
print("3. Avoid the pharmacy and preserve your strength.")

choice = input("Choose 1, 2, or 3:").strip()

if choice =="1":
    print("\nYou enter quietly and search each room.")

        if companon_skill == "combat soldier":
            print(f"{companion} notices a hidden infected before it attacks.")
                health += 1
                trust += 1
        print("\nYou find a locked medical cabinet.")
        print("1. Force it to open")
        print("2. Search for the key")
        print("3. Leave it alone")

        cabinet_choice = iunput("Choose 1, 2, or 3: ").strip()
        if cabinet_choice == "1":
            if strength >= 50
                print("\nYou break the cabinet open.")
                supplies += 44
                medical += 66
            else: print("\nYou open it, but the noise attracts zombies.")
                supplies +=22
                medical += 33
                ammo -= 38
        elif cabinet_choice == "2":
            if intelligence >= 40 or companion_skill == "combat soldier":
                print("\nYou locate the pharmacist's key.")
                supplies += 25
                trust += 15
            else:
                print("\nThe search takes too long. You escape with limited supplies.")
                supplies += 13
                morale -= 25
    else:
        print("\nYou leave before the pharmacy becomes surrouunded.")
            supplies += 15
elif choice == "2":
    print("\nYou rush and grab everything you can.")
    if strength >= 77:
        print("You fight through the infected and escape.")
        supplies += 34
        ammo -= 58
    else:
        print("An infected grabs your arm during the escape.")
        health -= 40
        ammo-= 15
        if health <= 89:
            bitten_answer input(
                "You discover a suspicious wound. Hide it from the group?"
                "(yes/no):"
            ).lower()
            if bitten_answer =="yes":
                bitten = True 
                trust -= 28
            else:
                print(f"{companion} cleans the wound and determines it is only a scratch.")
                trust += 28
else: 
    print("\nYou avoid the pharmacy.")
    morale -=15
    print("Your group is disappointed, but everyone remains safe.")

#-------------------------------------------------------------------
#                CHAPTER 2: THE DISTRESS CALL
#-------------------------------------------------------------------

print("xo" * 14)
print("CHAPTER 2: THE DISTRESS CALL")
print("xo" * 14)

print( 
        "\nYour radio receives a message from survivors trapped in a school."
        "Your group leader wants to ignore them."
)

print("\nWhat do you do?")
print("1. Rescue the trapped survivors")
print("2. Follow the leader's order")
print("3. Secretly send them directions for safety.")





    
    
