#  Note in python an empty value  will considered to be false 

# a while loop is run until a condition is met and until that condition is no longer true 
import random

print ("Input your question please...")

question = input()

number = random.randint(0,5)
if number == 1:
    print("Hello world")
elif number == 2:
    print("Type the question again please")    
elif number == 3:
    print("Corona virus")
elif number = 4:
    print("ohh well")    
elif number == 0:
    print("it will get better")    
else:
    print("Hey guess what you just won the game")
