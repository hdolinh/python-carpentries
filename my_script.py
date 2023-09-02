print("Hello World!")

# assigning values to vars
text = "Data Carpentry"
number = 42
pi_value = 3.1415

# use print() to display an outpu in a script
print(text)
print(number)

# operators
2 ** 16 # power
13 % 5 # modulo

# lists
# create using []
numbers = [1, 2, 3]
numbers[0] # indexing starts with 0

# add elements to a list using append()
numbers.append(4)

# tuples = immutable
# create using ()
num_tuple = (1, 2, 3)
str_tuple = ("blue", "green", "red")

len(num_tuple)
len(str_tuple)

# dictionaries = key, value pairs
# create using {}
translation = {"one": "first", "two": "second"}
translation["one"] # index using keys
translation["three"] = "third" # add a key, value pair
print(translation)
