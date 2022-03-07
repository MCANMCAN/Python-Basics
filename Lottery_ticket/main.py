import random
import replit
total_ticket={} # sums for manual loto numbers and automated loto numbers to bring a summary. 
auto_numbers={}
manual_numbers={}
def manual_checker(inp,list_manual): 
  if inp in list_manual:
    inp=int(input(f"You entered {inp} before, please input another one: "))
    manual_checker(inp,list_manual)
    return inp 
  else : 
    return inp
def randomer(liste):
  addition = random.randint(1,50)
  checker(addition, liste)
  return addition
def checker(number,liste):
  if number not in liste : 
    liste.append(number)
  else: 
    addition = randomer(liste)   
def random_generator(n): 
  a=1 
  i=0
  lottery_auto_number=[]
  lottery_auto_name = ""
  while n!=0:  
    lottery_auto_name = "autonumber"+ str(a)
    for i in range (0,6,1):
     addition = randomer(lottery_auto_number) 
     
    lottery_auto_number.sort() # to sort from desc order. 
    auto_numbers[lottery_auto_name] = lottery_auto_number #adds to number list by name of its ticket. 
    n = n-1
    a = a+1 # counter for ticket name 
    i = 0
    lottery_auto_number = []
  print(auto_numbers)
def manual_lotery():
  decision = True
  a=1
  i=0
  #lottery_manual_list =['_','_','_','_','_','_']
  
  while decision == True : 
    lottery_manual_name = "manuel" + str(a)
    lottery_manual_list =['_','_','_','_','_','_']
    for i in range(0,6,1): 
      num_limit = True
      inp_user = int(input(f"Please enter your a number between 1 and 49. ({6-(i)}) number(s) left: "))
      while num_limit == True:  
        if inp_user <= 49 and inp_user >0 : 
          num_limit = False 
        else: 
          inp_user = int(input(f"!!!!Out of limits!!!!Please enter a valid number between 1 and 49. ({6-(i)}) number(s) left: "))
          num_limit = True  

      number = manual_checker(inp_user, lottery_manual_list)
      lottery_manual_list[i] = number
      print(lottery_manual_list)
    lottery_manual_list.sort()
    manual_numbers[lottery_manual_name]= lottery_manual_list
    if input("Do you want to add another lottery ? 'y' to add or another key to exit : ") == 'y' : 
      decision = True
    else : 
      decision = False
    a+=1

if input("Would you like to use lotery generator? y or n :") == "y":
  random_generator(int(input("How many lotery would you like to generate?")))
manual_lotery()  

total_ticket = manual_numbers
print("manual_numbers=",manual_numbers)
total_ticket.update(auto_numbers)
nu=1
replit.clear()
print("TICKET SUMMARY ")
print("________________________________________")
for printer in total_ticket:
  print("________________________________________")
  print(f"N{nu} :",total_ticket[printer])
  print("________________________________________")

  nu+=1
print("________________________________________")