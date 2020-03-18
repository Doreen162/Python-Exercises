# Creating fizz buzz

for x in range(20, 2, -2):
    print(x)

else:
    print("I have complete my lesson in For loops")


for fizz_buzz in range(100):
    if fizz_buzz % 3 == 0 and fizz_buzz % 5 == 0:
        print("fizz_buzz")
        continue
    elif fizz_buzz % 3 == 0:
        print("fizz")
        continue
    elif fizz_buzz % 5 == 0:
        print("buzz")
        continue
    print(fizz_buzz)