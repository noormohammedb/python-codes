# method 1

"""import module2

print(__name__)

module2.sum(3,3)

fnc = module2.sum

fnc(4,4)"""

# method 2

"""import module2 as file2

print(__name__)

file2.sum(3,3)

fnc = file2.sum

fnc(4,4)"""


# method 2 only perticular funcion importing with from


from module2 import sum
from module2 import sum as fnc

print(__name__)

kkf = fnc

sum(3,3)
fnc(2,2)
kkf(9,9)
