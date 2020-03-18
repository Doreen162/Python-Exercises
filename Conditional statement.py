# speed limit allowed
speed = int(input("Please enter your speed: "))
average_speed = int(input("Enter allowed speed: "))

if speed <= average_speed:
    print("Ok good to go")

elif speed >= average_speed:
    demerit = speed - average_speed // 5
    print(demerit, "points")

if demerit >= 12:
    print("time to go to jail")