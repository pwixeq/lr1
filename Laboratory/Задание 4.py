t = (1,2,3)
try:
    t[1]=100
except:
    print('в кортеж нельзя присвоить элемент, тк котреж - неизменный тип данных')

t = (1,2,3)
a = (4,5)
t2 = t + a
print(t2)
print(t2.count(3))
print(t2.index(4))
print(t)
