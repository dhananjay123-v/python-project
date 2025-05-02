import random

print("Welcome In My Game :)")

playing=input("Do you want to play (yes/no) ?").lower()

if playing!="yes":
    quit()
    
print("Okey Lets Play ")

score=0
 
ans=input("Who Is the Prime Minister ? ").lower()
if ans=="modi":
    print("Correct !")
    score +=1
else:
    print("Incorrect !")


ans=input("Who Is the President ? ").lower()
if ans=="murmu":
    print("Correct !")
    score +=1
else:
    print("Incorrect !")
    
    
ans=input("Who Is the Home Minister ? ").lower()
if ans=="amitshah":
    print("Correct !")
    score +=1
else:
    print("Incorrect !")
    
print("You Got",score,"Out of 3")
print("Thank you for Playing :)")

