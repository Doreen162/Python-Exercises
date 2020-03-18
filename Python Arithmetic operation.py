# Exercise 1 Total amount of salary

salary = 1500
bonus = 200
commission = 0.02
laptops = int(input("enter number of laptops: "))
price = float(input("enter the price of a laptops:R  "))


bonus = (bonus * 10)
commission = (commission * 3000 * price)

salary = (salary + bonus + commission)
print(salary)




