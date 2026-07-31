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


