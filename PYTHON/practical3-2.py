# Relational & logical

a = 50
b = 20

print(a == b) #False
print(a != b) #True
print(a >= b) #True
print(a > b)  #True
print(a <= b) #False
print(a < b)  #False

# logical Not.
# "The Not oprator returns the opposite." 
# 1) Code :

print("Not oprator : ", not(True))
print("Not oprator : ", not(False))

# 2) Code :

a = 50
b = 30
print(not(False))
print(not(a > b)) #False

# logical AND.
# "The And operator says that if both var1 and var2 are True, then the AND oprator will give us a True output."
# 1) code :

val1 = True
val2 = True

print("and oprator : ", val1 and val2)

# 2) code :

val1 = True
val2 = False

print("and Oprator : ", val1 and val2)

# 3) code :

val1 = False
val2 = False

print("and Oprator : ", val1 and val2)

# logical or.
# "The OR oprator work in such a way that if either one Value or both values are True, the output will be True".

# 1) code :

var1 = True
var2 = True
print("or Oprator : ", val1 or var2)

# 2) code :

var1 = False
var2 = True
print("or Oprator : ", val1 or var2)

# 3) Code :
var1 = False
var2 = True
print("or Oprator : ", val1 or var2)

# 4) Code :

var1 = False
var2 = False
print("or Oprator : ", val1 or var2)

# 5) code :

a = 50
b = 30
print(not False)
print(not (a > b))

print("OR oprator : ", (a == b) or (a > b))

