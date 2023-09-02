print("Hello there!")
print("What is your name?")

myName = input()
print("It's nice to meet you, " + myName + ".")
print("I can tell you the length of your name is: " + str(len(myName)))
print("What is your age?")
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.") # str(int()) stores the input as a integer value instead of a string


# formatting strings
# three different ways

# one: use `str()`
print('I am ' + str(29) + ' years old.')

# two: use `{}` as a placeholder and `.format()`
print("I am {} years old.".format(29))

# three: create a var and `f`
age = 29
print(f"I am {age} years old.")
