
#the code below is written to ask the user details
#Welcoming the user
print("✨ Welcome to my Anime Quiz ✨")
print("This quiz is developed by Aryan Ghimeray")

# this function stores the dictionary containing questions, asks the user questions and marks the answer entered by the user and adds 1 score for every correct answer
def my_quiz():
  
#this dictionary stores the questions for the anime quiz
  
  questions = {'\n Which among the following anime was released first? \n A: Dragon Ball Z \n B: Pokemon\n C: Beyblade Metal Fusion\n': 'A', 
'\n Which among these is a real anime? \n A: Devil slayer \n B: Attack on Giants\n C: Naruto\n' : 'C',
'\n Which anime is Pikachu from? \n A: Pokemon \n B: Digimon\n C: Bakugan\n': 'A',
'\n Which year was the first episode of Naruto released in ? \n A: 2000 \n B: 2002 \n C: 2005 \n': 'B',
'\n Which country does anime originate from ? \n A: United States \n B: France \n C: Japan\n': 'C',
'\n What kind of wizard is Lucy in the anime Fairy tail? \n A: Celestial Wizard \n B: Fire Wizard \n C: Lightning Wizard\n': 'A',
'\n Who is the name of the main character of the anime Attack on Titan? \n A: Mikasa Ackerman \n B: Eren Yeager \n C: Levi Ackerman\n': 'B',
'\n Who is brother of Natsu Dragneel in the anime Fairy tail? \n A: Zeref Dragneel \n B: Jellal Dragneel \n C: Igneel Dragneel\n': 'A',
'\n Who turned Nezuko into a demon in the anime Demon Slayer? \n A: Kaigaku \n B: Akaza \n C: Muzan Kibutsuji\n': 'C',
'\n Which of the following is not a type of pokemon?\n A: Fire \n B: Ink \n C: Fairy\n': 'B', 
'\n What devil fruit has Luffy eaten in the anime One Piece? \n A: Gomu Gomu no Mi \n B: Yami Yami no Mi \n C: Mera Mera no Mi\n': 'A', 
'\n In the anime One Piece, who gave Luffy his straw hat? \n A: Whitebeard \n B: Mihawk \n C: Shanks\n': 'C', 
"\n What is the name of Goku's wife in the anime Dragon Ball Z? \n A: Chi-Chi \n B: Bulma \n C: Videl\n": 'A', 
'\n Whose son is Gohan in the anime Dragon Ball Z? \n A: Goku \n B: Vegeta \n C: Broly\n': 'A',
'\n Who is the main protagonist of the anime Sword Art Online? \n A: Asuna \n B: Kirito \n C: Eugeo\n': 'B'}

#this code loops the questions and marks the user input as correct or incorrect and gives the user +1 score for every question correectly answered
  score = 0
  for key in questions.keys():
   print("\n|------------------------|")
   player_answer=input(key).upper().strip()
   if questions.get(key)==player_answer:
    print("\nCorrect!")
    score+=1
    print("Your current score is " + str(score))
   else:
    print("\nIncorrect!")
  print("\nYou total score is " + str(score))
  print("\n|------------------------|")

 
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



#exit quiz
my_quiz()

