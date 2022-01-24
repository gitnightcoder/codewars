string = ""
check = string.lower()
# print(check)
flag = 0

for i in range(0, len(check)):
    for j in range(0, i):
        if check[i] == check[j]:
            flag = 1
            break
        j = j + 1
    i = i + 1
    
if flag:
    print('false')
else:
    print('true')