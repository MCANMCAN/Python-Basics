#Bankerroulette
import secrets
attenders=input("Enter name by space seperator, please \n")
attenders=attenders.title()
list_attenders = attenders.split(" ")
print(list_attenders)
luck_one = secrets.choice(list_attenders)
print(f"{luck_one} will pay today!")


#print(f"The unlucky one is {namelist(randomint(-1,5)" )
