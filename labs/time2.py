time = int(input("What is the current time (in hours 0-23)? "))
sleep = int(input("How many hours will you sleep? "))

alarm = (time + sleep) % 24
print("You will wake up at " + "{:.2f}".format(int(alarm)))
