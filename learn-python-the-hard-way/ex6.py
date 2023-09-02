# python has another kind of formatiing using `.format()`

# create a var `types_of_people` and set it to 10
types_of_people = 10
# create a var `x` and set it to a formatted string that
# has the var `types_of_people` within it
x = f"There are {types_of_people} types of people."

# create a var `binary` and set it to the string "binary"
binary = "binary"
# create a var `do_not` and set it to the string "don't"
do_not = "don't"
# create a var `y` and set it to a formatted string that
# has the vars `binary` and `do_not` within it
y = f"Those who know {binary} and those who {do_not}."

# prints out x
print(x)
# prints out y
print(y)

# prints out a formatted statement with the var `x` placed in it
print(f"I said: {x}")
# prints out a formatted statement with the var `y` placed in it
# `y` has single quotes around it
print(f"I also said: '{y}'")

# create var `hilarious` and set it to a boolean `False`
hilarious = False
# create var `joke_evaluation` and set it to a string and
# a placeholder for a var
joke_evaluation = "Isn't that joke so funny?! {}"

# prints out the string in `joke_evaluation` and the 
# var hilarious using `.format()`
# `.format()` fills the {} placeholder with whatever var it has
print(joke_evaluation.format(hilarious))

print(f"{joke_evaluation}{hilarious}") # see here the {} is empty

# create a var `w` and set it to a string
w = "This is the left side of..."
# create a var `e` and set it to a string
e = "a string with a right side."

# prints out both `w` and `e` and the strings they're set to
# prints out in specific order where `w` comes first and 
# `e` is added after `w`
# the `+` 'adds' both strings together
print(w + e)