print("! COFFEE MACHINE !\n")
machine_menu = {
  "americano": {"price" : 2, "water":220,"coffee":50,"milk":0 } ,
  "cappucino": {"price" : 4, "water":180,"coffee":50,"milk":50 },
  "latte": {"price" : 3, "water":180,"coffee":50,"milk":50 }
}
machine_stock = {"water":500,"coffee":250,"milk":120 }
#user selects a drink : 
def selection(menu): 
 for keys in menu: 
  print(f"{keys.capitalize()} ** Price : ${menu[keys]['price']} \n")  
 usr_in = input("What Would you like to drink ? \n").lower()   
 return usr_in
# report receipt of user .
def order_receipt(inp, pr, pb,pd): 
  print(f"{12*'*'} ORDER RECEIPT {12 *'*'}")
  print(f" USER SELECTION:{inp} \n",20*"--",f"\n UNIT PRICE :${pr}\n ",20*"--",f"\n  PAID :${pd} \n",20*"--",f"\n  CHANGE :${pb} \n")
def update_stock(usrin,machine_stock): 
  machine_stock["water"] -=machine_menu[usrin]["water"]
  machine_stock["coffee"] -=machine_menu[usrin]["coffee"]
  machine_stock["milk"] -=machine_menu[usrin]["milk"]
# report machine status .
def reporter(stock) : 
  print(f"{12*'*'} CURRENT STATUS {12 *'*'}")
  print(20*"--")
  for keys in stock :
    if keys != "coffee" : 
     print(f"The amount of {keys} = {stock[keys]} mL ")
    else : 
     print(f"The amount of {keys} = {stock[keys]} gr") 
    print(20*"--")
    #payment engine!!!!!!!
def payment_engine(price,bank=0) : 
  moneys ={"q": 0.25 ,"h":0.5 ,"f":1}
  print(f"select money below")
  for i in moneys : 
    print(f"{i} =${moneys[i]} \n")
  selected = input("Select type of your money : ")
  bank+= int(input(f"how money {selected}s do you want to add ?")) * moneys[selected]
  while input("Would you like to add another:(y/n) ").lower() == "y" :
    selected = input("Select type of your money : ")
    bank+= int(input(f"how money {selected}s do you want to add ?")) * moneys[selected]
    print(f"money added . Your total input : ${bank}")
  return bank    
#payment engine!!!!!!!**********************
def check_ingridients(req_list,stock):
  status=True
  if req_list[0] > stock["water"]: 
    status=False
  if req_list[1] > stock["coffee"]:
    status=False
  if req_list[2] > stock["coffee"]:
    status=False  
  return status
user_input = ""
payback =0
while user_input != "off" : 
  user_input= selection(machine_menu)
  if  user_input == "off": 
    print("machine shut down!")
    order_status = False
  elif user_input != "report" : 
    if user_input in machine_menu : 
      print(f"{user_input.capitalize()} selected")
      price = machine_menu[user_input]["price"] 
      req_ingridients=[machine_menu[user_input]["water"],machine_menu[user_input]["coffee"],machine_menu[user_input]["milk"]]
      order_status = check_ingridients(req_ingridients,machine_stock)
      if order_status == True : 
       print("Drink selected, please enter money")  
       entered_money = payment_engine(price, 0) 
       payment_status = False
       while payment_status == False : 
        if entered_money == price : 
          print("payment completed : " )
          payment_status = True
          update_stock(user_input,machine_stock)
        elif entered_money > price : 
          print("payment completed , you can receive your change. :" )
          payment_status = True
          payback = entered_money - price 
          print(f"${payback} is paid to the receive box.") 
          update_stock(user_input,machine_stock)
        else : 
          print(f"not enough, please add ${price-entered_money}")
          payment_engine(price,entered_money)
          payment_status = False
          
      else: 
        print("not enough ingredient, please try again later!")
      if order_status == True and payment_status==True : 
        print("Order Prepared ! You can take your drink! \n")
        order_receipt(user_input , price , payback,entered_money)
        input("\n enter a key for next order")  
  elif user_input == "report": 
    while user_input == "report":
      reporter(machine_stock)
      user_input = input("report generated , any key to continue!")



