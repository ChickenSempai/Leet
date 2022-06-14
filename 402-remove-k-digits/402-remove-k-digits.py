class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        i = 1
        while k>0:
            sizee = len(num)
            if i < len(num):
                while i < len(num) and k>0:
                    j = i
                    while j>0 and num[j-1] > num[i] and (i-j)<k:
                        j-=1
                    if j!=i:
                        num = num[:j] + num[i:]
                        # print(i, num)
                        k -= i-j
                        i = i-(i-j)
                        break
                    i+=1
            if len(num) == sizee:
                num = num[:len(num)-1]
                # print(i, num)
                i = len(num)-2
                k -= 1
            
            i+=1
            
        while len(num)>0 and num[0] == '0':
            num = num[1:]
        if len(num) == 0:
            num = '0'
        return num
            