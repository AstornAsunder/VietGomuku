import sys
import os
from os.path import dirname, abspath
import platform
from gc import collect
sys.path.append('C:\\Users\\Holly Lord\\PycharmProjects\\pythonProject')

# print(sys.path)


# print(__file__)
d = os.getcwd()
print(d)

d = dirname(dirname(abspath(__file__)))
print(d)
sys.path.append('/\\test_1')

print(sys.path)
print(platform.system())
print(platform.version())
print(platform.processor())

x = 11
if x > 10:
    b = 3
print(b)
del x
collect()
print(x)
s = 'String'

match s:
    case 'String':
        print('String')
    case 'This':
        print('Not string')

for i in range(11):
    match i:
        case 1:
            print(i)
        case 2:
            print(i)
        case 3:
            print(i)
            print('break')
            break
