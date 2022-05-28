import stdio

import math


num1 = int(input("please enter the first number "))
num2 = int(input("please enter the second number "))

value = ((num1 % num2 == 0) or (num2 % num1 == 0))
value = ((num1 % num2 != 0) or (num2 % num1 != 0))

stdio.writeln(value)


