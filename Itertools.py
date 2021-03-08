
from itertools import count
for i in count(2):
    print(i)
    if i >= 20:
        break


from itertools import accumulate

number = list(accumulate(range(6)))
print(number)

from itertools import takewhile
number = list(accumulate(range(8)))
print(number)
print(list(takewhile(lambda x: x<=6,number)))