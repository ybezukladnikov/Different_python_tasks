class Lec:
    array = [3, 4, 2, 4, 9]

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


print(Lec().last_in())