from collections import Counter
string = "sTreSS"
temp_str = string.lower()

res = Counter(temp_str)

for i in res:
    if res[i] == 1:
        print(i)
        break
