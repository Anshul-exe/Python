x = int (input ("a: "))
z = int (input ("b: "))
y = int (input ("c: "))
if x > y and x > z :
    print("largest no. is",x)
elif z > x and z > y:
    print("largest no. is",z)
else:
    print("largest no. is",y, "(putting variable in between)")
