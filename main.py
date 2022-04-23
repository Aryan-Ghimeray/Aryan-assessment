
#the code below is written to ask the user details
#Welcoming the user
print("✨ Welcome to my Anime Quiz ✨")
print("This quiz is developed by Aryan Ghimeray")

# this function stores the dictionary containing questions, asks the user questions and marks the answer entered by the user and adds 1 score for every correct answer
def my_quiz():
  
#question one 
  print("\nWhich among the following anime was released first?")
  answer_1 = input(" a: Dragon Ball Z\n b: Pokemon\n c: Beyblade Metal Fusion\n")
  if answer_1 == "a":
    print("\nCorrect!")
  else:
    print("\nIncorrect!")
    
  print("\nWhich among these is a real anime?")
  answer_2 = input("\n a: Devil Slayer\n b: Attack On Giants\n c: Naruto\n")
  if answer_2 == "c":
    print("Correct!")
  else: 
    print("\nIncorrect!")
    print("\nWhich year was the first episode of Naruto released?")
  answer_3 = input("\n a: 2000\n b: 2002\n c: 2005\n")
  if answer_3 == "b":
    print("\nCorrect!")
  else:
    print("\nIncorrect!")

    print("\nWhich country does anime originate from?")
  answer_4 = input("\n a: Brazil\n b: France\n c: Japan\n")
  if answer_4 == "c":
    print("\nCorrect!")
  else:
    print("\nIncorrect!")
    
  
# asks the user if they want to play again
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
     print("\n Please type 'Yes' if u want to replay the game and 'No' to exit the game.")
   
 
#asking user details (name and age)
#asking user name  
while True:
    name = input("Please enter your name here: ")
#this code checks that the user input is a letter, it will continue to ask for input until user enters a letter
    if name.isalpha():
        break
    print("Please enter name in alphabets only.")
    
#asking user age  
while True:
    age = input("Please enter you age here: ")
#this code tests that the user input is a number, it will continue to ask for input until user enters a number 
    if age.isnumeric():
      if 10< float(age)<130:
        break
      print("\nYou have to between the age of 10 and 130 to do this quiz.")
    print("\nPlease enter age in numbers only.")



#exit/replay quiz
my_quiz()
while re_play():
  my_quiz()
print("\n|------------------------|")
print("\n Thank you for playing 👋 ")
