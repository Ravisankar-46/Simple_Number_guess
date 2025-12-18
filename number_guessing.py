import random
y=input("Type a number: ")

if y.isdigit():
    y=int(y)
    if y<0:
        print("Please enter a positive number..")
        quit()
else:
      print("Please enter a positive number..")
      quit()      

x=random.randint(0,y)

gues=0
while True:
    guess=input("Guess a number: ")
    gues+=1
    if guess.isdigit():
       guess=int(guess)
      
    else:
         print("Please enter a positive number..")
         continue
       
    if guess==y:
           print("You did it")
           break
    else:
           print("Try again")

print("you take",gues,"attempts to find")