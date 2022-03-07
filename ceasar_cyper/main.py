alphabet = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'q', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z']
inp_list=[]
key=0
#print(inp_list) #for error handling
#encoder func starts
def encoder(text_input,keyin):
  text_output=""
  for i in range(0,len(text_input)):
    if text_input[i] == " ":
      text_input[i] = "_"
      #print(text_input) #for error handling
    elif not text_input[i] in alphabet: 
      text_input[i]= "$"
    else:
      if alphabet.index(text_input[i]) + keyin < len(alphabet):
        encoderr= alphabet.index(text_input[i]) + keyin
        text_input[i]=alphabet[encoderr]
        #print(encoderr) #for error handling
      else :
        #print(encoderr) #for error handling
        encoderr= alphabet.index(text_input[i]) + keyin - len(alphabet)  
        text_input[i]=alphabet[encoderr]
  text_output=text_output.join(text_input)
  print(f"Encription completed : \t{text_output}")
  #encoder ends
def decoder (text_input,keyin):
  text_output=""
  for i in range(0,len(text_input)):
    if text_input[i] == "_":
      text_input[i] = " "
#print(text_input) #for error handling
    elif not text_input[i] in alphabet: 
      text_input[i]= "$"
      #print(text_input) #for error handling
    else:
      if alphabet.index(text_input[i]) - keyin >= 0:
        if  alphabet.index(text_input[i]) - keyin == 0:
          encoderr=0
          text_input[i]=alphabet[encoderr]
        elif alphabet.index(text_input[i]) - keyin >= 31:
          encoderr=alphabet.index(text_input[i]) - keyin - len(alphabet)#-1
          #print(encoderr,"x") #for error handling
          text_input[i]=alphabet[encoderr]
        else:
          encoderr= alphabet.index(text_input[i]) - keyin
          #print(encoderr) #for error handling
          text_input[i]=alphabet[encoderr]
          #print(encoderr) #for error handling
      else :
        #print(encoderr) #for error handling
        encoderr= len(alphabet) -( keyin - alphabet.index(text_input[i]) )
        text_input[i]=alphabet[encoderr]
  text_output=text_output.join(text_input)
  print(f"Decription completed : \t{text_output}")


selection = int(input("Select opearation(1 or 2) : \n 1 for Encoder \n 2 for Decoder \n Selection: "))
inp = input("Please enter the text \n").lower()
key = int(input("Please enter the key : "))
inp_list = list(inp) 
if selection == 1: 
  encoder(inp_list,key)
if selection == 2:
  decoder(inp_list,key)