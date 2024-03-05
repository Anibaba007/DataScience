# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:02:59 2024

@author: user
"""
import math
dir(math)
for name in dir(math):
  print(name, end="\t")


from math import pi, radians, degrees, sin, cos, tan, asin
g = 90
ar = radians(g)
ad = degrees(ar)

print(g == 90.)
print(ar == pi / 2.)
print(sin(ar)/cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

import random
dir(random)
from random import random
for i in range(5):
    print(random())

# The seed function
from random import random, seed

seed(0)

for i in range(5):
    print(random())

# The randrange and randint functions
from random import randrange, randint

print(randrange(1), end= ' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

from random import randint
for i in range(40):
    print(randint(1, 30), end=',')

# The Choice and sample function
from random import choice, sample
my_list = [16,15,28,17,9,2,26,30,18,30,1,3,24,27,13,23,27,26,22,21,1,20,16,27,28,11,8,24,11,23,28,3,7,30,19,8,8,26,5,26]
print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))









