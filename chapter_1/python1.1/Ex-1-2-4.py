import stdio

a = 3

b = 4

com1 = (a < b)

com2 = (a > b)

com3 = (not(com1))
 
com4 = (not(com2))

com5 = (com3 and com4)


stdio.writeln(com5)

stdio.write((not(a < b) and not (a > b)))