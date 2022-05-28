import stdio


# let a and b values as given
a = True
b = False


value = (not(a and b) and (a or b)) or ((a and b) or not (a or b))

stdio.write(" value1 " )
stdio.writeln( value )

 # let a and b values as given
a = True
b = True


value = (not(a and b) and (a or b)) or ((a and b) or not (a or b))

stdio.write(" value2 " )
stdio.writeln( value )

 # let a and b values as given
a = False
b = True


value = (not(a and b) and (a or b)) or ((a and b) or not (a or b))

stdio.write(" value3 " )
stdio.writeln( value )



 # let a and b values as given
a = False
b = False


value = (not(a and b) and (a or b)) or ((a and b) or not (a or b))

stdio.write(" value4 " )
stdio.writeln( value )