import random 
from data_base import data 
from art import vs
def first_game(): 
  a = random.randint(0,len(data)-1)
  b = random.randint(0,len(data)-1)
  while a==b : 
    b = random.randint(0,len(data))
  print(f"\nName : {data[a]['name']}--Description:{data[a]['follower_count']} -- Country: {data[a]['country']}--> u")
  print(vs)
  print(f"\nName : {data[b]['name']}--Description:{data[b]['follower_count']} -- Country: {data[b]['country']}--> d")
  #if data[b]['follower_count'] > data[a]['follower_count'] : 
    
  #return [b,a]
  #else : 
  return [a,b]
def next_game(ndx) : 
  up = ndx
  down = random.randint(0,len(data)-1)
  while up==down : 
    down = random.randint(0,len(data)-1)
  print(f"\nName : {data[up]['name']}--Description:{data[up]['follower_count']} -- Country: {data[up]['country']}--> u")
  print(vs)
  print(f"\nName : {data[down]['name']}--Description:{data[down]['follower_count']} -- Country: {data[down]['country']}--> d")
  #if data[down]['follower_count'] > data[up]['follower_count'] : 
  #  return [down,up]
  #else : 
  return [up,down]
#def winner_decider(): 
is_game_on = True 
started =False
n=0 #score counter 
while is_game_on == True : 
  if started == False  : 
   started = True
   fist_list = first_game()
   up   = fist_list[0] 
   down = fist_list[1]
   if data[up]['follower_count'] > data[down]['follower_count']: 
     winner = 'u' 
     winner_index = up
   else : 
     winner = 'd'  
     winner_index = down
   #print(winner)
  else:
   user_input=input("Please enter your decision , up or down ? (enter u or d )\n")
   if user_input == winner :  
    n=n+1 
    print(f"SCORE : {n} {100*'/'}\n Nice! continue") 
    next_list = next_game(winner_index)
    up = next_list[0] 
    down = next_list[1] 
    if data[up]['follower_count'] > data[down]['follower_count']: 
     winner = 'u' 
     winner_index = up
    else : 
     winner = 'd'  
     winner_index = down
   else : 
    n=0 
    started = False
    winner_index ="" 
    is_game_on = False 
    print("Wrong answer, game over!")
