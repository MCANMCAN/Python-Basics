
summ=0
for n in range(2,101,2):
 print(n)
 summ=summ+n
print(summ,'\n')

summ=0
for n in range(1,101):
  print(n)
  if n % 2 == 0: 
    summ+=n
print(summ,'\n')
