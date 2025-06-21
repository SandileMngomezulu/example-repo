age=int(input("Please input a age between 1 to 100: "))
if age > 100:
    print("Sorry, you are dead.")
elif age >= 65:
    print("Enjoy your retirement")
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrets you are 21st!")
elif age < 13:
    print("Yot qualify for the kiddie discount.")
else:
    print("Age is but a number")