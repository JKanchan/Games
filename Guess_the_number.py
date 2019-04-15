#!/usr/bin/python
import random

num = random.randint(0,9)
i = 0;
print(num);
print("Guess the number")
while(i<6):    
    x = input()
    if(x == str(num)):
        print("YaY! you won");
        break;
    else:
        print("Try once again")
    i += 1;
    
#print(i);
if(i==6):
    print("Sorry you are out of guesses");
    print("The correct number is :" + str(num));
    


     
