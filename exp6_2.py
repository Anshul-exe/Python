#Without Recursion
def fac_without_recursion(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
num = int(input("Enter your number: "))
print("Factorial of",num,"is",fac_without_recursion(num))