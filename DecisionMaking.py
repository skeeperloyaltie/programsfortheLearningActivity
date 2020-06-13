#Python Conditionals
#Conditionals and Booleans

#If statements
print("If statements")

name = str(input("Enter your last name: "))

year = int(input("Enter your year of birth: "))

current_year = 2020

age = int(current_year - year)

if (age >= 20 ):
    print("Welcome to adulthood dear " + name)
print("Dear " + name + ",Your age is: " + str(age)) 

#if_else
print("if_else statements")

eng = int(input("Enter first subject marks: "))

maths = int(input("Enter second subject marks: "))

kiswa = int(input("Enter third subject marks: "))

avg = (eng + maths + kiswa)/3

s = "The student got "
if (avg >= 70):
    print(s + "A")
elif (avg >= 60):
    print(s + "B")
elif (avg >= 40):
    print (s + "D")
elif (avg <= 39):
    print(s + "E")
else:
    print("Input correct values")

#loops
print("Loops in python")

#while_loop
print("The while Loop")
x = int(input("Enter a number between 0 and 20 "))

while(x<10):
    x = x + 1
    print("Number will add a one until its 10")
    print(x)
else:
    x = x - 1
    print("The number is greater than 10")
    print(x)

#for_loop
print("The for_loop")

v = ("Skeeper", "is", "in", "love")

for i in v:
    print(i)  

#dictionaries
print("Dictionaries:")
d = dict()

d['A'] = 1
d['B'] = 2
d['C'] = 3

for f in d:
    print("%s" %(f))

import pprint, os
d = {
    1: {'name': 'Godfrey'},
    2: {'name': 'Gudah'},
    
}

for a, b in d.items():
    print(a,b)
while True:
    print("Type a name: ")
    name = str(input (name.lower()))

    if ( name =='Godfrey'):
        print('I am a Skeeper')
        exit()
    elif ( name == 'Gudah'):
        print("I am Bouyant")
        exit()

#using else statements in  for_loop


print ("Enter a number between 0 and 100 ")

y = int(input())
for c in range (y):

    for c in range (0, 50):
        if (c < 50):
            print("Fuck niggas")
            exit()
    for c in range (51, 100):
        if (c > 50):
            print("They fuckin messed me")
            exit()
        exit()
#using continue in  for loops

print ('Using Continue in for loop')
print("Enter your name: ")

x = str(input())
for letter in x:
    if letter == 'e' or letter == 's':
        continue
    print ('Current letter :', letter)
    var = 10
#using break
    if letter == 'y' or letter == 'd':
        break
    print ('Current word is: ', letter)


    #Using pass
for letter in x:
    pass
print ('Last letter : ', letter)






    



