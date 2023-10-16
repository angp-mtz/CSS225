# Angelyque Martinez
# 10.14.2023
# Program is intended to run 7 problems from the course lab in CSS 225
# For instructors James Cottrell and Benjamin Page


print("Hello World") # problem 1 - prints hello world

print(' ')

name = input("what is your name? ") # problem 2 - greets user
print("greetings, ", name)

print(' ')

name_2 = 'Ang' or 'James' or 'Benjamin'
confirm = input("please confirm your name again:  ") # problem 3 - greets instructors and i
if confirm == name_2:
    print("greetings, ", name_2)
else:
    print("who are you?")

print(' ')

pi = 3.1415926535897932384626433
radius = float(input("what is the radius of the circle? ")) # problem 4 - calculates area of circle
area = pi * radius**2
print("okay, the area of the circle is:", area)

print(' ')

miles = float(input("what is the number of miles driven? ")) # problem 5 - calculates MPG of car
gallons = float(input("now, what is the number of gallons used? "))
MPG = miles / gallons
print("your mpg is: ", MPG)

print(' ')

fahrenheit = 'F'
celcius = 'C'
convert = input("convert to fahrenheit (F) or celcius (C) degrees?: ") # problem 6 - converts temperature F and C
if convert == fahrenheit:
    tempC = float(input("enter the temperature: "))
    print("the conversion is: ", ((tempC * 9/5) + 32))
if convert == celcius:
    tempF = float(input("enter the temperature: "))
    print("the conversion is: ", ((tempF - 32) * 5/9))

print(' ')

def week(day): # problem 7 - returns day of return
    if day == 0:
        return "sunday"
    elif day == 1:
        return "monday"
    elif day == 2:
        return "tuesday"
    elif day == 3:
        return "wednesday"
    elif day == 4:
        return "thursday"
    elif day == 5:
        return "friday"
    else:
        return "saturday"

start_day = input("what is the day (0[sunday] to 6[saturday]? ")
length = input("what is length of stay? ")
calc1 = int(start_day)
calc2 = int(length)
total = (calc1 + calc2) % 7
print("will return on the day" , str(week(total)))
