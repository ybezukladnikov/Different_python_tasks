class Selection_sort:
    def selection_sort(self, array):
        for i in range(0, len(array)):
            min_index = i
            for j in range(i + 1, len(array)):
                if array[min_index] > array[j]:
                    min_index = j

            array[i], array[min_index] = array[min_index], array[i]

        return array

    def insert_sort(self, array):
        for i in range(0, len(array)):
            j = i + 1
            while (j < len(array) - 1):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]
                    j = i + 1
                j += 1
        return array

    def quick_sort(self, array, start, stop):
        if stop - start <= 1:
            return
        ind_pivot = (stop - start) // 2
        print(ind_pivot)
        ind_left_ch = ind_pivot
        ind_right_ch = ind_pivot
        i = start
        j = stop
        while (i < ind_pivot or j > ind_pivot):

            while i < ind_pivot:
                if array[i] > array[ind_pivot]:
                    ind_left_ch = i
                    i += 1
                    break
                i += 1
                ind_left_ch = i

            while j > ind_pivot:
                if array[j] < array[ind_pivot]:
                    ind_right_ch = j
                    j -= 1
                    break
                j -= 1
                ind_right_ch = j

            array[ind_left_ch], array[ind_right_ch] = array[ind_right_ch], array[ind_left_ch]
            print(array)
        self.quick_sort(array,ind_pivot+1, stop)
        self.quick_sort(array, start, ind_pivot - 1)


array = [9, 3, 1, 2, 0, 3, 2, 1, -23]
array1 = []
# print(Selection_sort().selection_sort(array))
# print(Selection_sort().insert_sort(array))

Selection_sort().quick_sort(array, 0, len(array) - 1)
print(array)
