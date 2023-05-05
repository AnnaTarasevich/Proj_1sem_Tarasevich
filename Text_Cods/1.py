list1 = [1, 5, 8, 12]
print(list(map(lambda x: x - 2, list1)))

print(list(filter(lambda x: x*2 == 10, list1)))

from functools import reduce

print(reduce(lambda x,y: x*y, list1))

f = [2, 10, 15, 30]
z = [x*2 for x in f]
print(z)

l = [4, 10, 12, 3]
d = [y**2 if y % 2 == 0 else y*2 for y in l]
print(d)

u = [2, 5, 6, 12, 8]
c = ["rkbf", "dw", "wdw", "wd"]
s = [8, 15, 3, 12]
rel = zip(u,c,s)
print(list(rel))

k= [4,10,5]
kr = iter(k)
print(type(k))
print(type(kr))
print(dir(k))
print(dir(kr))
print(next(kr))
print(next(kr))
print(next(kr))
print(next(kr))