import stdio
import math

numT = int(input(" please enter value for tempreture"))
numV = int(input(" please enter value for speed"))

w = 35.74 + (0.6215 * (numT)) + (0.4275 * (numT) - 35.75) * numV**0.16

stdio.writeln(w)