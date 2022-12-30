array = [14, -2, -5, 12, 8]

if array[0]>array[1]:
    max_first = array[0]
    max_second = array[1]
else:
    max_first = array[1]
    max_second = array[0]

for el in array[2:]:

    if el > max_first:
        max_second = max_first
        max_first = el
    elif el > max_second:
        max_second = el

print(max_second)