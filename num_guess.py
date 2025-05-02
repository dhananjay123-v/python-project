import random

top_num=input("Enter Num :")

if top_num.isdigit():
    top_num=int(top_num)
    
    if top_num <= 0:
        print("please type number greater than 0")
        quit()
else:
    quit()
    
ans=random.randint(0,top_num)
score=0
while True:
    user_guess=input("Enter Guess :")
    score +=1
    if user_guess.isdigit():
        user_guess=int(user_guess)
        
    if ans==user_guess:
        print("Congratulation Correct !")
        break
    elif user_guess>ans:
        print("too high")
    else:
        print("too low")

print("You Got in",score,"Time  Guess")

    