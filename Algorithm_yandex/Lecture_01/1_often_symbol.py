str = 'ddfdseekkfr'

class FindOftenSymbol:
    def find(self, str):
        ans = 'String is empty'
        count = 0
        if len(str):
            dict_sym = {}
            for el in str:
                if el not in dict_sym:
                    dict_sym[el] = 0
                dict_sym[el] += 1
            for sym, cnt in dict_sym.items():
                if cnt > count:
                    ans = f"Often symbol '{sym}' meet {cnt} times"
                    count = cnt

            print(ans)
        else:
            print(ans)


FindOftenSymbol().find("aasdfdddfsss")
