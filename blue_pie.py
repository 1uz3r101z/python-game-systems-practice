# FLAGS/STORY MEMORY 
#--Remembering what the player has done--

flags = {
  "met_Batman": False,
  "read_letter": False,
  "saved_friend": False
}
flags["read_letter"] = True 

if flags ["read_letter"]: 
  print("You recognize the handwriting.")
else: 
    print("The handwriting means nothing to you.")
