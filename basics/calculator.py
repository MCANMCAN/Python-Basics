def multip(no1,no2):
  return no1*no2
def addition(no1,no2):
  return no1+no2
def division(no1,no2):
  return no1/no2
def substraction(no1,no2):
  return no1-no2
operations = {
  "*": multip ,
  "/": division,
  "+": addition,
  "-": substraction
}
def calculator_start():
 num1 = float(input("please input first number! : "))
 lopper ="y"
 lopper_b= True
 result =0
 while lopper_b == True:
    for operation in operations : 
     print(operation)
    operate= input("Please input an math operation above : ")
    num2 = float(input("please input second number! : "))
    result=round(operations[operate](num1,num2),2)
    print(f"{result} is calculated by {num1} {operate} {num2}")
    
    lopper =input(f"press 'k' continue with {result} , 'y' to start new calculation, another key to exit : ")
    if lopper == "k":
     num1= result
    elif lopper == "y":
     lopper_b = False
     calculator_start()
    else: 
      lopper_b = False
calculator_start()