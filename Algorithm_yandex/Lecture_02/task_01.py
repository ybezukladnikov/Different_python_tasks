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


print(Lec().max_number())