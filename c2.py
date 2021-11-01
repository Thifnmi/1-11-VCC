import random
# print(random.randint(1,100))
listnumber = []
lists = []
for _ in range(100):
	listnumber.append(random.randint(1, 100))

for i in listnumber:
	if(i < 10):
		lists.append(listnumber[i])

for i in range(len(lists)):

	if(lists[i] % 2 == 0):
		lists[i] = "chan"
	elif(lists[i] % 2 != 0):
		lists[i] = "le"
print(f"list ban dau: {listnumber} có {len(listnumber)} phần tử, list dau filter {lists} có {len(lists)} phần tử ")