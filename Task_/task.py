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



# print(DifTask().super_shift([1,2,3,4,5,6], 8))


array = [4, 2, 4, 1, 7, 9, 3, -4]

# print(list(filter(lambda el: el < 0, array)))


n = int(input())  # 1 <= n <= 100 000 | Amount of tanks
Volumes = list(map(int, input().split()))  # Volume of each tank
answer = 0
maximal = Volumes[0]
for i in range(len(Volumes)):
    maximal = max(Volumes[i], maximal)
    if Volumes[i] < maximal:
        answer = -1
        break
print(max(Volumes) - min(Volumes) if answer == 0 else answer)




