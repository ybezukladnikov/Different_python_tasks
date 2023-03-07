import timeit
class Fibonachi:
    def get_dig_fib_rec(self, num):
        if num == 1:
            return 1
        elif num == 0:
            return 0
        else:
            return self.get_dig_fib_rec(num - 2) + self.get_dig_fib_rec(num - 1)


    def get_dig_fib(self, num):
        res = [0, 1]
        if num == 0:
            return 0
        if num == 1:
            return 1
        for i in range(2,num+1):
            res.append(res[i-1]+res[i-2])
        return res[num]
n = int(input("Input number => "))
# time_start = timeit.default_timer()
# print(Fibonachi().get_dig_fib_rec(n))
# print(timeit.default_timer() - time_start)
time_start = timeit.default_timer()
print(Fibonachi().get_dig_fib(n))
print(timeit.default_timer() - time_start)
