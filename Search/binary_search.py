
array = [i for i in range(0,101)]
stop = len(array)-1



class Search:
    def binary_search(self, array, num, start, stop):
        mid_point = (stop - start)//2 + start
        if (stop - start) < 0:
            return -1
        else:
            if array[mid_point] == num:
                return mid_point
            elif num > array[mid_point]:
                return self.binary_search(array, num, mid_point + 1, stop)
            elif num < array[mid_point]:
                return self.binary_search(array, num, start, mid_point - 1)



print(Search().binary_search(array,100,0,stop))