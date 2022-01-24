my_str = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
numbers = my_str.split()
size = len(numbers)

intlist = map(int, numbers)

res = list(sorted(intlist))
my_ans = []
my_ans.append(res[size-1])
my_ans.append(res[0])

temp_res = [str(int) for int in my_ans]
str_res = ' '.join(temp_res)
print(str_res)