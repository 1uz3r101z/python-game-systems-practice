# MULTIPLE ENDINGS 

trust = 7 
saved_friend = True 

if trust => 5 and saved_friend:
  print (" GOOD ENDING")
elif trust < 0: 
  print("BAD ENDING")
else:
  print("NEUTRAL ENDING")

print("xo"*10)

print("xoxo ZOMBIE APOCALYPSE XOXO")
print("You have reached the final night.\.n")

trust = int(input("What is your group's trust level (0-10)?"))
saved_friend = input("Did you save your friend? (yes/no): ").lower() == "yes"
found_cure = input("Did you find the Zombie cure? (yes/no): ").lower() == "yes"
romance = int(input("What is your romance level (0-10)?:))

if found_cure and saved_friend and trust >= 8:
  print("\nSECRET ENDING")
  print("You use the cure to stop the outbreak.")
  print("Humanity survives because of you.")
elif romance >= 7 and saved_friend:
  print("\nROMANCE ENDING")
  print("You escape with the person you love.")
  print("Together, you search for a safe place beyond the infected zone.")
elif trust >= 5 and saved_friend:
  print("\nGOOD ENDING")
  print("Your group fights through the hoarde and reaches safety.")
elif trust <= 2 and not saved_friend:
  print("\nBAD ENDING")
  print("Your group is gone. Your friend is gone.")
  print("You hear zombies approaching from behind...")
else:
  print("\nCHAOTIC ENDING")
  print("Nothing went according to plan")
  print("You jump into an abandoned truck and drive straight through the horde.")
  print("You have absolutely no idea where you're going.")
  
    
                    



                  


