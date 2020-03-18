# Creating loops on Python

cars = ["BMW", "VW", "FORD", "NISSAN"]
for x in cars:
    print(x)

# My list of cars

cars = ["BMW", "VW", "FORD", "NISSAN"]
for theList in cars:

    if theList == "VW":
        break
        print(theList)

# My list of bikes

Bikes = ["honda", "yamaha", "KTM", "bmw"]
for theCars in cars:
    for theBikes in Bikes:
        print(theCars, theBikes)

# My list of numbers

for number in range(1, 11):
    print(number)

# My list of numbers
for numbers in range(2, 22, 2):
    print(numbers)
else:
    print("we have finished lesson on loops")

