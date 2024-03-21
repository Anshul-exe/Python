string = (input("Enter your sentence: \n"))
count = 0
for i in range (0, len(str)):
    if(string[i] !=''):
        count = count + 1;
print ("Total no. of characters are ", +str(count));