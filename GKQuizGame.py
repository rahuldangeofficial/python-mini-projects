#GKquizgame
print("\033c") #clear screen

print("GK Game for Kids between Age 4-7 Years")
playing=input("You want to play? (yes/no) ")


if playing.lower()!="yes":
    quit()
    
print("\033c") #clear screen
score=0

x=input("1. How many days do we have in a week? ")
if x.lower()=="seven" or x.lower()=="7":
    print("Correct!")
    score+=1
else:
    print("Wrong")
    
print("\033c") #clear screen

x=input("2. How many colors are there in a rainbow? ")
if x.lower()=="seven" or x.lower()=="7":
    print("Correct!")
    score+=1
else:
    print("wrong")
    
print("\033c") #clear screen    

x=input("3. How many letters are there in the English alphabet? ")
if x.lower()=="twenty six" or x.lower()=="26":
    print("Correct!")
    score+=1
else:
    print("wrong")
    
print("\033c") #clear screen

x=input("4. How many sides are there in a triangle? ")
if x.lower()=="three" or x.lower()=="3":
    print("Correct!")
    score+=1
else:
    print("wrong")

print("\033c") #clear screen
    
print("Your total score is "+str(score))
print("You got "+str((score/4)*100)+"%")

