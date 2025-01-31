# Asking AI a question: Here’s a comprehensive list of all built-in types in Python, categorized by their type groups:
#
# 1. Numeric Types
# int: Integer (whole numbers)
# float: Floating-point numbers (decimals)
# complex: Complex numbers (with real and imaginary parts)
# 2. Sequence Types
# str: Strings (text data)
# list: Ordered, mutable sequence
# tuple: Ordered, immutable sequence
# range: Immutable sequence of numbers
# 3. Text Type
# str: String (already mentioned under Sequence Types)
# 4. Set Types
# set: Unordered collection of unique elements
# frozenset: Immutable version of set
# 5. Mapping Type
# dict: Key-value pairs
# 6. Boolean Type
# bool: Logical values (True, False)
# 7. Binary Types
# bytes: Immutable sequence of bytes
# bytearray: Mutable sequence of bytes
# memoryview: View over a bytes object
# 8. None Type
# NoneType: Represents the absence of a value (None)
# 9. Special Types (Type Hints)
# Any: Any type (used for type annotations)
# Union: Multiple possible types (Union[int, str])
# Optional: Type or None (Optional[str])
# Literal: Specific literal values (Literal["yes", "no"])
# 10. Built-In Functions Returning Types
# type: Returns the type of an object
# object: Base type for all classes
# chapter 1 --- overall I think we had pretty similar methods of solving these exercises, but I do think the professor had a better method of printing the results and I will have to start implementing that method
r42 = round(42.5)
r43 = round(43.5)
print(r42, r43)
# python rounds to the nearest even number
print(2++2)
print(2+-2)
# print(4 2) # SyntaxError: invalid syntax. Perhaps you forgot a comma?
# round(42.5 SyntaxError: '(' was never closed
# round 42.5 SyntaxError: invalid syntax
print(type(765), type(2.718), type('2 pi'), type(abs(-7)), type(abs(-7.0)), type(abs), type(int), type(type))
# Guesses: 765 integer, 2.718 float, '2 pi' string, abs(-7) integer, abs(-7.0) float, abs function, int type, type type
seconds = 42*60+42
miles = 10/1.61
seconds_per_mile = seconds/miles
minutes_and_seconds = seconds_per_mile/60
average_speed = 1/(minutes_and_seconds/60)
print(seconds, miles, seconds_per_mile, minutes_and_seconds, average_speed)
# Chapter 2 --- my excercise 1 was better because the professor didn't include the 12 = n question, but his printing is still better... for exercise 2 I could have improved my answer by using a if statement like the one the professor used. 
import math
# 17 = n illegal - a variable cannot start with a number
x = y = 1 # legal
print("my dog ate my python code"); # code still runs, but a little yellow bar appears below semi-colon
# print(64). SyntaxError: invalid syntax
# import maath ModuleNotFoundError: No module named 'maath'
pi = math.pi
radius = 5 # radius in centimeters
volume = (4/3)*pi*radius**3 # volume in cubic centimeters
print(volume)
x = 42
print((math.cos(x))**2+(math.sin(x))**2) # it is true, but the professors version was much cooler using the if statement
print(math.e**2, math.pow(math.e, 2), (math.exp(2))) # using my calculator I also computed these values, and it seems like the last one is correct