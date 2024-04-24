#With Recursion
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
num=int(input("Enter your number: "))
print("Your answer is", factorial(num))