
array = [i for i in range(0,101)]
stop = len(array)-1



class Search:
    def binary_search(self, array, num, start, stop):
        midle = (stop - start)//2
        find_ind = start + midle
        if array[find_ind] == num:
            return find_ind
        elif num > array[find_ind]:
            start+=midle
            return self.binary_search(array, num, start, stop)
        elif num < array[find_ind]:
            stop-=midle
            return self.binary_search(array, num, start, stop)



print(Search().binary_search(array,24,0,stop))