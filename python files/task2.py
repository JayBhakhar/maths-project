## TASK 6.9.14 ##

import itertools

lst = []
num = int(input("input number for permutations :- "))
for n in range(num):
    n = n + 1
    lst.append(n)

for p in itertools.permutations(lst):
    print(''.join(str(x) for x in p))
