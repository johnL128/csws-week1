#Simple Hello World Program with loop
for i in range (10):
    print ("Hello World " + str(i))
    
#Simple Arithmetic
for x in range (5):
    y = 5 + x
    print (y)
    
#Simple List (Array)
names = ["Harry", "Dara", "Ethans Mum", "sam"]
print (names)

#.title() capitalises first letter of the str
print (names[3].title())

#Everything
for i in range (4):
    print ("Hello " + names[i])

#A bunch of random places
places = ['Shetland','Manila','Milan','Stockholm']

print(sorted(places))

places.reverse()

print(places)

places.reverse()
places.sort()
print(places)





