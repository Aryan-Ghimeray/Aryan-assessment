
#Welcoming the user
print("✨ Welcome to my Anime Quiz ✨")
print("This quiz is developed by Aryan Ghimeray")


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

#printing all users details 
print("Hello",name,"your age is",age)
print()
questions = {'Which anime was released first? \n A: Dragon Ball Z \n B: Pokemon\n C: Beyblade\n': 'A', 'Which muic was released first? \n A: Dragon Ball Z \n B: Pokemon\n C: Beyblade\n': 'A' }



for key in questions.keys():
  player_answer=input(key).upper().strip()
  if questions.get(key)==player_answer:
    print("Correct!")
  else:
    print("Incorrect!")



