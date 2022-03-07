
for i in range(1,31):
  if i<3 : 
    print(i)
  if i >=3:
    if i % 3 == 0 and i % 5 == 0 : 
      print("FizzBuzz!!")
    elif i % 3 == 0: 
      print("FIZZ!")
    elif i % 5 == 0: 
      print("BUZZ!")
    else : 
      print(i)

for i in range(1,31):
 if i % 3 == 0 and i % 5 == 0 : 
  print("FizzBuzz!!")
 elif i % 3 == 0: 
  print("FIZZ!")
 elif i % 5 == 0: 
  print("BUZZ!")
 else : 
  print(i)