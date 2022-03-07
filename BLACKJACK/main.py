import random
#from replit import clear
def hand_check(lst):
  if 11 in lst and sum(lst)>21 : 
    lst.remove(11) 
    lst.append(1) 
  return lst 
def cpu_game(cpuhand):
  if sum(cpu_hand)<17: 
    return "y"
  else: 
    return "n"
# listeden rastgele kart çeker .
def card_picker(gamer_list) : 
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  nw_card = random.choice(cards)  
  gamer_list.append(nw_card)
  return gamer_list
restarter = 'y'
while restarter == 'y':
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_hand=[]
  cpu_hand=[]
  for _ in range(2):
   new_card = random.choice(cards)
   user_hand.append(new_card)
   new_card = random.choice(cards)
   cpu_hand.append(new_card)
  print(f"Your Hand: {user_hand}")
  print(f"Cpu Hand:  [* ,{cpu_hand[1]}]")
  new_card=0
  # as kartı özel sayıdır. el 21den küçükse 1 , 21'i geçerse 1 değeri alır. 
  is_game_on = True
  user_hand = hand_check(user_hand)
  cpu_hand = hand_check(cpu_hand)
  user_decision=True
  
  # kartlar dağıtıldığında 21 olan bir oyuncu varsa oyunu kazanır! 
  if sum(user_hand) == 21 or sum(cpu_hand)== 21 : 
    if sum(user_hand)==21 : 
      print("Blackjack!! User Wins!")
      is_game_on = False
    elif sum(cpu_hand) == 21 : 
      print("BlackJack !! CPU wins ")
      is_game_on = False
  else:
    user_decision = input("Want to pick a card or stay = \n 1- y for pick \n 2- n   for stay : ").lower()
  # fonksiyonları kullanarak oyunu oynatacak olan loop 
  while is_game_on == True : 
    if user_decision == 'y' and sum(user_hand) <= 21: 
      user_hand = card_picker(user_hand)
      hand_check(user_hand)
    else : 
      user_decision == 'n'
    cpu_decision = cpu_game(cpu_hand) 
    if cpu_decision == 'y' and sum(cpu_hand) < 21: 
      cpu_hand = card_picker(cpu_hand)
      hand_check(cpu_hand)
      print("Computer picked a card") 
    else : 
      cpu_decision == 'n'
      #tüm kart çekimleri bittiği için kazanan ile birlikte eller açık olarak   gösterilmeli ! 
    if user_decision != 'y' and cpu_decision != 'y': 
      print(f"CURRENT STATUS : \n USER'S HAND :{user_hand}\t Total: {sum  (user_hand)}\n CPU'S HAND :{cpu_hand}\t Total: {sum(cpu_hand)}")
      is_game_on = False
    # kartlar çekildikten sonra kullanıcıya genel durumu veren bir output. 
    print("___________________________________")
    print(f"CURRENT STATUS : \n USER'S HAND :{user_hand}\t Total: {sum(user_hand)}  \n CPU'S HAND :[*{cpu_hand[1:]}\t")
    # eğer iki taraftan biri 21i aşarsa loopu bitirmek için aşağıdaki if: 
    if sum(user_hand)>21 or sum(cpu_hand)>21: 
      is_game_on = False
    # oyuncunun yeni kart seçmesi için gerekli şartlar sağlanıyor mu: 
    if user_decision == 'y' and sum(user_hand)<21 and is_game_on==True:
      user_decision = input("Want to pick a card or stay = \n 1- y for pick \n 2-n for stay : ").lower()
    #tüm kart çekme işlemleri biterse ,veya bir oyuncu 21i aşarsa uygun outputu   verecek olan değerlendirme yapılır. 
    if is_game_on == False:
      #clear()
      print("USER_HAND:",user_hand)
      print("CPU_HAND:",cpu_hand)
      if sum(user_hand)>21: 
        print(f"User Picked {user_hand[-1]} ")
        print("USER LOST! YOUR HAND > 21")
      elif sum(cpu_hand)>21 : 
        print("CPU BUSTED! USER WINS")
      elif sum(user_hand)>sum(cpu_hand): 
        print("YOUR HAND IS BIGGER THAN CPU'S HAND . USER WINS")
      elif sum(cpu_hand)>sum(user_hand) : 
        print("CPU'S HAND IS BIGGER THAN USER'S HAND . CPU WINS")
      else : 
        print("DRAW")
  restarter= input("Do you want to restart the game? (y or n) : ").lower()