## 6.9.9

from itertools import combinations


n = []
num = int(input("input n :- "))
for m in range(num):
    m = m + 1
    n.append(m)

def Set(arr, r):
	return list(combinations(arr, r))

if __name__ == "__main__":
	arr = n
	r = int(input("input r = "))
	print(Set(arr, r))



