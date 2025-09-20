from copy import deepcopy

num = [7, 2, 5]
num.append(4)
print(num)
num.insert(1, 10)
print(num)
num.extend([1,1,1])
print(num)
num.remove(7)
print(num)
num.pop(-1)
print(num)
num.sort()
print(num)
num.reverse()
print(num)
c = num.count(2)
print(c)
i = num.index(1)
print(i)
cop = num.copy()
print(cop)
cop2 = deepcopy(num)
print(num)
num.clear()
print(num)


