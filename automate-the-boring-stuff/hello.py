print("Hello there!")
print("What is your name?")

myName = input()
print("It's nice to meet you, " + myName + ".")
print("I can tell you the length of your name is: " + str(int(len(myName))))
print("What is your age?")
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.")

# formatting strings
# three different ways
print('I am ' + str(29) + ' years old.')
print("I am {} years old.".format(29))