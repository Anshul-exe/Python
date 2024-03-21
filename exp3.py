print("Your equation is 1+x+x²+x³...+xⁿ ")

x= float( input("Now enter your value for x: "))
y = int( input("Enter your power: "))

sum = 0

for i in range(y+1):
    sum=sum + x**i

print("Sum of the series is: ",sum)