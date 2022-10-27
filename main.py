#how many cookies do you have
print("How many cookies do you have?")
cookie = int(input())
if cookie < 3:
    print("You don't have enough cookies")
elif cookie > 3 and cookie < 10:
    print("You have a good amount of cookies")
else:
    print("You have too many cookies! Give me one!")
print()
#jedi or sith(or breadstick)?
print("Are you a Jedi or Sith?")
js = input()

if js == "Jedi" or js == "jedi":
    print("You get a green lightsaber!")
elif js == "Sith" or js == "sith":
    print("You get a red lightsaber!")
else:
    print("You get a breadstick!")
    
print()
#for loop
for i in range(4, 40, 2):
    print(i, end = " ")
print()
print()
#While loop from 100 to 50
x = 100
while x >=50:
    print(x)
    x -= 10

#knock knock, orange
while True:
    print("Knock Knock...")
    print("Who's there?")
    choice = input()
    if choice == "orange" or choice == "Orange":
        print("Orange you glad I didn't say banana")
        break
    else:
        print("BANANA")
print()
#multiplication function
def multiply(x, y, z):
    a = x*y*z
    return a

print("2 x 3 x 4 = ", multiply(2,3,4))

print()
#rootbeer on the wall
def rootbeer(x):
    for i in range(x):
        print(x, " bottles of root beer on the wall...")
        x -= 1
        
print("give me a number: ")
r = int(input())
print(rootbeer(r))
