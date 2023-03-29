class Lec:
    array = [3, 45, 12, 4, 9]


    def first_in(self):

        search = int(input("Input number => "))
        ans = -1
        for i in range(len(self.array)):
            if self.array[i] == search and ans == -1:
                ans = i
        return ans

    def last_in(self):
        search = int(input("Input number => "))
        ans = -1
        for i in range(len(self.array)):
            if self.array[i] == search:
                ans = i
        return ans

    def max_number(self):
        ans = 0 if len(self.array) else -1
        if ans != -1:
            for i in range(1, len(self.array)):
                if self.array[i] > self.array[ans]:
                    ans = i

        return self.array[ans]

    def max_second_number(self, array):
        first_max = max(array[0], array[1])
        second_max = min(array[0], array[1])

        for i in range(2, len(array)):
            if array[i] > first_max:
                second_max = first_max
                first_max = array[i]
            elif array[i] > second_max:
                second_max = array[i]

        return second_max


print(Lec().max_second_number([2, 2, 4]))