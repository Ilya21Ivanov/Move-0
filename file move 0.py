#[0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
#[0] -> [0]
#[1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
#[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

lst = [0, 1, 0, 12, 3]

x = len(lst)
lst1 = 0
for i in range(x):
    if lst[i] != 0:
        lst[lst1] = lst[i]
        lst1 += 1

for i in range(lst1, x):
    lst[i] = 0
print(lst)

lst = [0]

x = len(lst)
lst1 = 0
for i in range(x):
    if lst[i] != 0:
        lst[lst1] = lst[i]
        lst1 += 1

for i in range(lst1, x):
    lst[i] = 0
print(lst)

lst = [1, 0, 13, 0, 0, 0, 5]

x = len(lst)
lst1 = 0
for i in range(x):
    if lst[i] != 0:
        lst[lst1] = lst[i]
        lst1 += 1

for i in range(lst1, x):
    lst[i] = 0
print(lst)

lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

x = len(lst)
lst1 = 0
for i in range(x):
    if lst[i] != 0:
        lst[lst1] = lst[i]
        lst1 += 1

for i in range(lst1, x):
    lst[i] = 0
print(lst)



