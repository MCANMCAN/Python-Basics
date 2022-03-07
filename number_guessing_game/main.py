import random
from replit import clear
def question():
 q = random.choice(range(1,101))
 #print(q)
 #print(ans ,'*')
 return int(q)
# user decides the number of attempts as difficulty.
def difficulty_selector():
  false_input=False
  while false_input==False:
   diff=input("Select a difficulty \n - Easy(e) \n - Hard(h) : ").lower()
   if diff == 'e' : 
     print("Game started in easy difficulty. ")
     false_input=True  
   elif diff == 'h' : 
     print("Game started in hard difficulty. ")
     false_input=True  
   else: print("Wrong entry please enter e or h")
  return diff
"______________________________________________________________________________"
# decides life according to user input . 
def life_check(): 
  ans = difficulty_selector() 
  if ans == 'h':
   return 5 
  elif ans =='e':
   return 10
# num_check
def valid_check(no):
  try: 
      no=int(no) # trying to transfor input to integer . 
      is_valid = True
  except ValueError:# on error , comes here and decides it cannot be converted to number
      print("You entry is not a number!")  
      is_valid = False # boolean goes to our game that number is not valid. 
  if is_valid != False:
    if no > 100 or no<1 : # if input is a number checks if the number is in limit. 
      print("You entry is out of limit!")
      is_valid = False
  return is_valid #if true our game can use the number . 
def new_number(life):
  new =input(f"Please enter a new valid number . You have {life} left: ")
  return new
# game engine
is_game_on = True 
while is_game_on == True : 
  user_input = "" # if empty program understand it is first entry. 
  life = life_check() 
  validity = False  # the number validity check variable. 
  answer = question()
  #print(f"Troubleshooting : {answer}")
  while life>0 and is_game_on == True : # loop for main game 
    while life>0 and validity == False : # asks input till user enters valid number
     user_input = new_number(life) 
     validity = valid_check(user_input) 
    
    user_input = int(user_input) # if valid number , transforms input to integer . 
    if user_input == answer :  # check input according to statements below. 
      print(f"You win. The guessed the number {user_input}")
      is_game_on = False #ends the game if user finds the answer
    elif user_input/2 >= answer :
      print(f"{user_input} is too big than the answer:( \n{40*'_'}\n")
  
    elif user_input > answer : 
      print(f"{user_input} is bigger than the answer:(\n{40*'_'}\n")
    elif answer/2 >= user_input : 
      print(f"The answer is too big than your guess :(\n{40*'_'}\n")
    elif answer >= user_input :
      print(f"The answer is bigger than your guess :(\n{40*'_'}\n")
    
    life-=1 # reduce life in every answer
    if life==0 and is_game_on == True: 
      print(f"You are out of life!\n{40*'_'}\n") 
      is_game_on = False #ends the game if user cannot find the answer and do not hava another life. 
    # print(life)  # for error checking
    validity = False #resets validity of input to start next numbers validity check.
  d =input("Do you want to play again? y to play again... \nor another key to exit. : ").lower() # ask user to restart game
  if d == 'y':  
    is_game_on = True 
    clear() # clears terminal if the new game starts