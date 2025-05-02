# import random

#NOTE program to print coin probality
# coin = random.choice(["Head","Tail"])
# print(coin)

#NOTE program to print random number between x to y probality
# num = random.randint(1,10)
# print(num)

#NOTE shuffle the value of the string
# cards =["Munna","Dhananjay","Aditya"]
# cards =[1,2,3,4,5]
# random.shuffle(cards)
# print("OTP ",end="")
# for i in cards:
#     print(i,end=" ")


#NOTE: return float value x to y with 10 desimal value
# c=random.uniform(20,30)
# print(c)

#NOTE: return float value 0 to 1 with 10 desimal value
# print(random.random())



# Import statistics Library
# import statistics

# # Calculate average values
# print(statistics.mean([1, 3.9, 5, 7, 9.4, 11, 13]))
# print(statistics.mean([1, 3, 5, 7, 9, 11]))
# print(statistics.mean([-11, 5.5, -3.4, 7.1, -9, 22]))


# # Calculate middle values
# print(statistics.median([1, 3, 5, 7, 9, 11, 13]))
# print(statistics.median([1, 3, 5, 7, 9, 11]))
# print(statistics.median([-11, 5.5, -3.4, 7.1, -9, 22]))


# # Calculate the mode

# print(statistics.mode([1, 3.9, 5, 7, 9.4, 11, 13]))
# print(statistics.mode([1, 1, 3, -5, 7, -9, 11]))
# print(statistics.mode(['red', 'green', 'blue', 'red']))


import sys    
if len(sys.argv)<2:
        print("Less argument")
elif len(sys.argv)>2:
        print("To many argument")
else:
        print("hello My name Is", sys.argv[1])