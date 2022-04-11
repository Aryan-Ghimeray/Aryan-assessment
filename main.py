
#the code below is written to ask the user details
#Welcoming the user
print("✨ Welcome to my Anime Quiz ✨")
print("This quiz is developed by Aryan Ghimeray")

# -------------------------
def my_quiz():
   print("\n To answer the question, please select the letter corresponding to the options.")
   for key in questions.keys():
    player_answer=input(key).upper().strip()
    if questions.get(key)==player_answer:
     print("Correct!")
    else:
     print("Incorrect!")
    
questions = {'\n Which anime was released first? \n A: Dragon Ball Z \n B: Pokemon\n C: Beyblade\n': 'A', 
'\n Which among these is a real anime? \n A: Devil slayer \n B: Attack on Giants\n C: Naruto\n': 'C', 'Which among these is a fake anime? \n A: Devil slayer \n B: Attack on Giants\n C: Naruto\n': 'C'}

# --------------------------

def re_play():
  while True:
   reply = input("\n Do you want to play the game again? \n Yes or No?: \n")
   reply = reply.upper() 

   if reply == "YES":
    return True
   if reply == "NO":
    return False
    break
   else:
     print("\n Please ype 'Yes' if u want to play the game and 'No' to exit the game.")
   
# --------------------------
 
#asking user details (name and age)
#asking name using 
while True:
    name = input("Please enter your name here: ")
    if name.isalpha():
        break
    print("Please enter name in alphabets only.")

#asking age using 
while True:
    age = input("Please enter you age here: ")
    if age.isnumeric():
      if 10< float(age)<130:
        break
      print("You have to between the age of 10 and 130 to do this quiz.")
    print("Please enter age in numbers only.")
#---------------------------



my_quiz()
while re_play():
  my_quiz()
print("\n Thank you for playing")
