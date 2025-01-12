import numpy as np

#a
a = np.zeros((3,3))
a[2,:] = 1
print('a)')
print(a)

#b
b = np.zeros((3,3))
b[1:,1] = 1
print('b)')
print(b)

#c
c = np.zeros((3,3))
c[1:,:] = 1
print('c)')
print(c)

#d
d = np.zeros((3,3))
d[:2,(0,2)] = 1
print('d)')
print(d)

#e
e = np.zeros((3,3))
e[1:,1:] = 1
print('e)')
print(e)