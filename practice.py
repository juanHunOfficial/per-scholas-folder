example_of_int = 10

example_of_str = "10"

example_of_float = 10.01

example_of_dict = {
    "name" : "Juan",
    "age" : 28,
    "scared_or_confident_in_python" : "confident" 
}

example_of_array = [ 1, 2, 3, "Example", "of", "strings", 10.01231, {"name" : "Juan", "age" : 28}] #this is to showcase that you can do store multiple values in an array

# This is known as a comment, programmers use this to document their work in plain english. Comments are completely ignored by the machine when the 
# code is ran. This purely used for documentation purposes. 

# The following lines of code is a progression to showcase the introduction to reading and understanding code. 

# Intro to functions and the 'input' function

value = input("Everything within the quotes is printed to the screen for the user to see and respond. Enter a number: ")
###### This line will be displayed with a cursor at the end, indicating that it is waiting on a response.
###### The reason for this functionality is the function named 'input'. think back to algebra "f(x) = x + 1"
###### Similar to this the function returning a particular OUTPUT (the result after you solved for 'x')
###### there is also an INPUT that needs to be given, this is similar to when you are given x (like 'Solve for x where x = 3')
###### Now you start to see where your algebra classes and above now come in handy. Take a big sigh of relief because you often
###### times will not be asked to do complex math, it is this functionality that you will be using. 

# Now on to reading code. With the brief introduction to values and functions out of the way, you may be tempted to read code
# the same way you read a book. Often times this is fine but you need to be able to recognize how to read code in the order of 
# operation. Similar to how you have the order of operations when solving in math (PEMDAS = Please Excuse My Dear Aunt Sally/ Power Exponent Multiplication Division Add Sub)
# programming has something similar, take this function below for example:

value = int(input("Enter a value: "))
# This is NOT read as follows: "value equals int input and whatever you get back from input.". 
# Instead this read as follows : "the user's input is entered and turned into and int and stored in the value variable".
# There was a progression going from right to left, in the order that the function is required to run. It must started from the right and work its way
# to the right. First, I need the value from the 'input' function in order to pass a value to the 'int' function (think f(x) 
# I cant pass x if i dont have know what it is). Second, now that we received the value from the 'input' function we are not about to pass that value (the 'x' in f(x))
# to the 'int' function. Now int can do its job and return the value as an integer (that is what int does essentially). Finally, we can now assign (this is 
# how you should read a single '=') the value we received from the 'int' function to the 'value' variable.



# Finally, you can see the results of what you just did by using the print function. Again look at it as f(x)
# 'print' is 'f' and 'value' is  'x'. You should the number you entered earlier.
# NOTE: if you did not enter a complete number you will get an error because it is not an integer...
print(value)

#############################################################################################################################################

string_example = "this is just an example of a value"

# What does it mean when we say everything in python is an Object.
# in VS Code and many other text editors, you can press '.' at the end of the 'string_example', it should look like this 
# 'string_example.' there should be a list of possible functions attached to the string that can be used like capitalized. 
# so string_example.capitalize() will make the lowercase 't' into a capital 'T'. 

print(string_example.capitalize())

# This '.' after the variable name is known as dot-notation. It is a way to access the functions within the object. 
# So within 'string_example' there are multiple string functions within it, thats what that list was that you saw after adding the period at the end of 
# the 'string_example' variable. This is what it would actually look like in code:
#
#   string_example = {
#       capitalize() : "The code needed to run this function",
#       lower() : "The code needed to run this function"
#   }
# 
# To see what this looks like under the hood, hold the 'ctrl' key (Windows/Linux) 'command' key (MacOS) and click on capitalize in VS Code. 
# this will take you to the code that, behind the scenes, has been automatically applied to the 'string_example' variable when it was created;
# specifically to the function called 'capitalize()'. The over all structure that your looking at is known as an object. 
# Notice that the capitalize function is under the class 'str'. This is basically saying, the object is of type 'str' or string. 
# The functions that are nested within it are assigned to the class and can be accessed through the object created using '.' dot-notation.
# BUT WAIT, I thought this was an OBJECT not a CLASS. Yes, if this seems confusing, the simple answer that is you need to understand as a beginner is this:
# a CLASS is a function that creates OBJECTS. Ok now how does this look? In other older languages like Java, when you create a string variable, it 
# does not do the same thing. In Java it basically makes a snapshot of the variable in memory(RAM) and it looks somewhat like this:
# 'string_example is of type str', and thats it! There are no functions added under the hood, it is not an object it is just another piece of data
# that the computer is tracking through memory. 
#
################################################################################################################################################

# Brief intro to the most used Data Structures. 
# There are more data structures than what I'll be listing here. These are the data structures that can carry you to an intermediate level. 
# The other data structures are more niche and although they are more optimal at a high-level, these basic data structures can accomplish 
# similar end results. 
#
# First we need to cover PRIMITIVE DATA TYPES
# Primitive data types are simply variables that can only hold one piece of data at a time and is represented by a single type. 
# An example is string_example = "Everything within these quotes is one piece of data assigned to the string_example variable."
#
#### Here are the Primitive Data Types:
#
# String - otherwise known as 'str' anything represented by a set of single or double quotes like this: "This is one piece of data". 
#       NOTE: a number that is in a set of double or single quotes, is still a string it is not an int or float and contains no numeric value
#             For example: value1 = "10" is not the same as value2 = 10. Below is a code snippet that will output to the terminal what the types 
#             are
#
value1 = "10"
value2 = 10
print(f"This is of type string ---->    {type(value1)}")
print(f"This is of type int ------->    {type(value2)}")
#
# Integer - otherwise known as 'int' a whole number (not a decimal) that is NOT contained by a set of single or double quotes. 
#       NOTE: if you try to do some kind of division or multiplication with decimals you need to use a float data type which is covered next.
#             doing division with a single forward slash '/' will convert your value to a float automatically. To divide two integers you need
#             to use double forward slash '//'. This is known as integer division.
#
# Float - otherwise known as 'float', it is simply the decimal version of int. Floats are used for accuracy, things like programs that deal with
#         money or calculations for things that need super precise representation down to the last decimal. 
#
# Boolean - otherwise known as 'bool', it is simply the evaluation of True or False. A boolean value is either True or False nothing more. 
#
# None - this is simply the absence of a value, common when we receive missing data.
#
#### DATA STRUCTURES:
# Array - otherwise known as a list in Python. An array is used to hold multiple values, of any type of primitive data types in whatever order you want.
#         You can identify an array by square brackets [] and each values within is separated by commas ','. You can see an example of this noted below.
#   EXAMPLE: 
array_example = []
# This is an example of an empty list (array). And below this is what it looks like when you fill the array with values.
#   EXAMPLE:
array_example = [1, 2, 3, "this is a string", 10.1234]
# This is an example of list filled with different data types. The main thing you need to take note of is the structure of this data types.
# Think of as an actual list of items, now it is IMPORTANT to notice, the values inside of the list are not variables them selves, they 
# are individual pieces of data within the list. 'array_example' is the variable, that holds these 5 values within the square brackets []
# and separated by commas ','
#
# Dictionary - otherwise known as 'dict', a dict is a data structure that uses something called 'key value pairs'. What this means is if I
#              wanted to access any form of data within the dict I would need to make the request by telling it which 'key' I want to retrieve.
#              You can identify a dict by looking for curly braces {}, and each value in the dict is separated by commas ','.
#              Here's an example of an empty dict
dict_example = {}
#
# Here is an example of a dict with some values.
dict_example = {
    "example_key": "example value", # this is one key value pair 'key : value' notice the key is separated from the value by a colon ':'.
    52 : "fifty two"
}
#
# Here is an example how you would access the dict if I wanted the 'fifty two' value. 
print(dict_example[52])
# NOTE: accessing a dict you need to use what is called bracket notation which you can see is simply adding square brackets [] to the end 
#       of the variable, also remember if I wanted the value "example value", I would need to access it exactly in the same format I made the key
#       So this is what it would look like in code:
print(dict_example["example_key"])
#
# Tuple - This is the easiest data type to understand but it is also the most restrictive. A tuple is easily identified by a set of parenthesis () 
#         and the values inside are separated by commas, there is one key difference with this data structure. 
#         IMPORTANT: Tuples are immutable, that means that once this has been declared it will not change. It will throw an error. The only way is to
#                    completely overwrite the value, below is an example of this in real time. Notice the difference in the numbers of IDs.
tuple_example = (1,2,3)

print(id(tuple_example))
print(tuple_example)

tuple_example = (4,5,6)

print(id(tuple_example))
print(tuple_example)
#
# However, I cannot change the value for the tuple. Example below:
tuple_example[0] = 20 # This should be the resulting error!!!!! <--------------------------------