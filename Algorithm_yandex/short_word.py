my_array = ['d', 'ss', 'ee', 'd', 's']

len_word = len(my_array[0])
res = []

for i in my_array:
    if len(i) == len_word:
        res.append(i)
    elif len(i) < len_word:
        res = [i]

print(' '.join(res))