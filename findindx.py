# arr = [3, 7, 2, 9, 5,10]

# largest = arr[0]

# for i,value in enumerate(arr):
#     if value > largest:
#         largest = value


# print(largest)


num1 = [1,2,2,1]
num2 = [2,2]

n1 = []

for i in num1:
    if i not in n1:
        n1.append(i)

n2 = []

for i in num2:
    if i not in n2:
        n2.append(i)

n3=[]
for num in n2:
    if num in n1:
        n3.append(num)

print(n3)

print(n1)
print(n2)


