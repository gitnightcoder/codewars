from collections import Counter
from gettext import find

find_it = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

res = Counter(find_it)

print(res)

for i in find_it:
    if find_it.count(i)%2!=0:
        print(i)
        break

