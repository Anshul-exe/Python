from collections import defaultdict

test_list = ["Hello hello hello!!", "hello everyone can you please", "Hello My name is Anshul"]

print("The original list is : " + str(test_list))

temp = defaultdict(int)

for sub in test_list:
	for wrd in sub.split(): 
		temp[wrd] += 1

res = max(temp, key=temp.get)

print("Word with maximum frequency : " + str(res))