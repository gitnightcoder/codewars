string = "The sunset sets at twelve o' clock."

answer = []
for char in string:
    if char.isalpha():
        answer.append(ord(char) & 31)
    else:
        pass
    
print(' '.join([str(i) for i in answer]))