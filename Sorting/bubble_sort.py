from Array import initial_array


count = 0
def buble_sort(array):
    global count
    size = len(array)
    for i in range(size):
        for j in range(size-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            count+=1



print(f'Initial array => {initial_array}')
buble_sort(initial_array)
print(f'Sorted array => {initial_array}')
print(count)
