# NUMBERS LESSON

# Python numbers are a group of four data types: plain integer, long integer, floating - point and complex numbers.
num = 10 + 5j  # The number object got created.
print(num)
# (10 + 5j)
type(num)  # The number is of complex type.
# < class 'complex'>
id(num)  # The initial address of 'num' in memory.
# 10171888
num = 11 + 6j  # The 'num' gets a new value.
print(num)
# (11 + 6j)
type(num)  # The 'num' is still of complex type.
# <class 'complex'>
id(num)  # Change in value caused 'num' to have a new memory address.
# 10171952

# Types of Numbers in Python
# Python 2.x had four built - in data types(int, long, float and complex) to represent numbers.
# Later Python 3.x removed the long and extended the int type to have unlimited length.

# The int type - represents the fundamental integer data type in Python.
# The plain integer in Python 2.x had the maximum size up to the value of sys.maxint.
# While in 3.x, the int type got promoted to have unlimited length and thus eliminated the long.
x = 9
type(x)
# < type 'int' >

# The long type - An integer number with unlimited length.Until the end of Python 2.x, the integers were allowed to overflow and turned into a long.This behavior changed since 3.0, where the ints replaced the longs.
x = 9999999999
type(x)  # In Python 2.x, the type will be long. While in 3.x, it is int irrespective of the size.
# < type 'long' >

# The float type - represents a binary floating point number.Using a float variable in an expression automatically
# converts the adjoining longs and ints to floats.
x = 9.999
type(x)
# < type 'float' >

# The complex type - The number of this type has a real and an imaginary part.
# For example – The expression(n1 + n2j) represents a complex type where both n1 and n2 are the
# floating-point numbers denoting the real and imaginary parts respectively.
x = 3 + 4j
type(x)
# <class 'complex'>
x.real
# 3.0
x.imag
# 4.0

# The number types are automatically upcast in the following order. Int → Long → Float → Complex
# While integers in Python 3. x can be of any length, a float type number is only precise to fifteen decimal places.
# Usually, we work with numbers based on the decimal (base 10) number system.But sometimes,
# we may need to use other number systems such as binary (base 2), hexadecimal (base 16) and octal (base 8).In
x = 0b101
print(x)
# 5
type(x)
# < type 'int' >
print(0b101 + 5)
# 10
print(0o123)
# 83
type(0x10)
# < type 'int' >

# test the class type of a number in Python, then you should use the isinstance() function. isinstance(object, class )
# Here is the example.
isinstance(2.2, float)
# True
# If you use mixed data types in an expression, then all operands will turn to behave as the most complex type used.
2 + 3.8
# 5.8
# Be careful while dividing integers in Python.
# In Python 2.x, the division( /) will return an integer quotient as the output.
7 / 2
# 3
# In Python 3.x, the division( /) will return a float quotient as the output.
7 / 2
# 3.5

# The  floor operator( //) returns the integer quotient, and the mod( %) operator gives the remainder.
# However, you can get both these by using the divmod() function.
divmod(7, 2)
# (3, 1)
7 % 2
# 1
7 / 2
# 3.5
7 // 2
# 3

# Type conversion(casting) in Python
# In Python, it is pretty easy to convert any numeric data type into another.
# We call this process as coercion in Pythonic term.

# Basic operations such as addition, subtraction coerce integer to float implicitly(by default) if one of the operands is a float.
2 + 4.5
# 6.5
# In the above example, the first integer(2) turned into a float(2.0) for addition, and the output is also a floating point number.
# Number of built - in functions such as int(), float() and complex() to convert between types explicitly.
int(3.7)
# 3
int(-3.4)
# -3
float(3)
# 3.0
complex(4 + 7j)
# (4 + 7j)

# External classes to handle Python numbers
1.1 + 3.2
# 4.300000000000001
# To overcome such type of issues, we can use the decimal module in Python.

# Python Decimal
# The decimal module provides the fixed and floating point arithmetic implementation which is familiar to most people.
# Unlike the floating point numbers which have precision up to 15 decimal places, the decimal module accepts a user - defined value.
# It can even preserve significant digits in a number.
import decimal
print(0.28)
print(decimal.Decimal(0.28))
print(decimal.Decimal('5.30'))

# Python Fractions - Python packages a module named as ‘fractions,’ to handle fractional numbers.
# Example to create and use fraction type objects.
import fractions
print(fractions.Fraction(2.5))
print(fractions.Fraction(5.2))
print(fractions.Fraction(3, 5))
print(fractions.Fraction(1.3))
print(fractions.Fraction('3.7'))

# Python mathematics
# Python exposes a few built - in functions to carry out simple mathematical calculations.
# For example – abs(), cmp(), max(), min(), round().
print(round(55.26, 1))
print(round(66.36, -1))
# Output –
# 55.3
# 70.0

# We can also use the math module in Python.It provides following common functions to use.

# Function    Description
# abs(x)      The absolute value of x: the(positive) distance between x and zero.
# ceil(x)     The ceiling of x: the smallest integer not less than x
# cmp(a, b)   - 1 if a < b, 0 if a == b, or 1 if a > b
# exp(x)      The exponential of x: ex
# floor(x)    The floor of x: the largest integer not greater than x
# log(x)      The natural logarithm of x, for x> 0
# log10(x)    The base - 10 logarithm of x for x> 0.
# max(x1, x2,…)    The largest of its arguments: the value closest to positive infinity
# min(x1, x2,…)    The smallest of its arguments: the value closest to negative infinity
# modf(x)     The fractional and integer parts of x in a two-item tuple. Both parts share the same sign as x.The integer part coerces into a float.
# pow(x, y)   The value of x ** y
# round(x[, n])    x rounded to n digits from the decimal point.
# sqrt(x)     The square root of x for x > 0
# pi          The mathematical constant pi.
# e           The mathematical constant e.

# Example - 1
import math
x = math.ceil(3.5)
print(x)
print(math.ceil(2 + 4.2))
# Output –
# 4
# 7

# Example - 2
from math import ceil
x = 9 / 4
y = ceil(x)
print(y)
# Output –
# 3