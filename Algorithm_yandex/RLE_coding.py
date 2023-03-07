string = 'AABBXRUUzzzU'

def rle(s):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s
    ans = []

    lastsym = s[0]
    lastpos = 0
    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append(pack(lastsym, i - lastpos))
            lastsym = s[i]
            lastpos = i
    ans.append(pack(lastsym, len(s) - lastpos))
    return ''.join(ans)


print(rle(string))