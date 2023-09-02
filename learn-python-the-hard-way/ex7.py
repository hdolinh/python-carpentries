print("Mary had a little lamb.")
# prints out string and the end of the string has a placeholder using `{}`
#  we use `.format()` to fill in the place holder with 'snow'
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
# prints out 10 periods because we've multiplied '.' by 10
print("." * 10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') # without end=' ' "Cheese" and "Burger" are on two different lines
# prints out all the end7-end12 vars as if they've been added together
print(end7 + end8 + end9 + end10 + end11 + end12)

# my question: I'm not sure how the second print statement knows to stay on the same line. 
# I know end=' ' is creating a space and without it 'Burger' is on a new line.