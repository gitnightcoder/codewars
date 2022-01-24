test_string = "Hello world"
words = test_string.split()

result = []

for item in range(len(words)):
    if words[item][0].isalpha() == True:
        result.extend([words[item][1:], words[item][0], 'ay',' '])
    else:
        result.append(words[item][0])


s = ''
s = s.join(result)
print(s.rstrip())



'''print(words)
print(words[3][3])'''