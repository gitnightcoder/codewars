from inspect import stack


string = "hi())("

count = 0
for i in string:
    if i == '(':
        count += 1
    elif i == ')':
        count -= 1
    elif count < 0:
        return False
        
return count == 0