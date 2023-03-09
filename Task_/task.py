class DifTask:
    def super_shift(self, array, num_shift):
        size = len(array)
        flag_1, flag_2 = 1, 1
        if num_shift < 0:
            flag_1 = 0
            flag_2 = -1
        if abs(num_shift) > size:
            num_shift = (abs(num_shift) % size) * flag_2
        new_array = [0 for _ in range(size)]
        for i in range(size):
            new_array[i+num_shift-size*flag_1] = array[i]

        return new_array



print(DifTask().super_shift([1,2,3,4,5,6], 8))






