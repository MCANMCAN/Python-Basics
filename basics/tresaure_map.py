
row1 = ["⬜️"," ⬜️","⬜️"]
row2 = ["⬜️"," ⬜️","⬜️"]
row3 = ["⬜️"," ⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#print(len(position)) # added for error handling
col=int(position[1])-1 # -1 because is used for list indexing
row=int(position[0])-1 # -1 because is used for list indexing

if len(position) < 2 or len(position) >= 3: #checking the number of character is two digit string
  print("Address not found! Please enter two digit number between 11 and 33 ")
else:
  if int(position[0])<= 0 or int(position[0])>= 4: # checks input is not out of range in our 3x3 table. 
    print("Address not found! Please enter two digit number between 11 and 33 ")
  elif int(position[1]) <= 0 or int(position[1]) >= 4: # checks input is not out of range in our 3x3 table. 
    print("Address not found! Please enter two digit number between 11 and 33 ")
  else:
    map[row][col]=" X"
    print(f"{row1}\n{row2}\n{row3}")


