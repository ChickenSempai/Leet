class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        field = [0 for i in range(32)]
        for n in nums:
            b = map(int, '{:0{size}b}'.format(n if n>0 else n+(1<<32), size=32))
            i=0
            for bb in b:
                if bb:
                    field[i] +=1
                    if field[i] == 3:
                        field[i] = 0
                i+=1
        if field[0]:
            k=0
            for i in range(1,33):
                k=i 
                if field[-i] == 0:
                    field[-i] = 1
                else:
                    break
            
            field[-k]=0
            for i in range(32):
                if field[i]:
                    field[i] = 0
                else:
                    field[i] = 1
            res = -int("".join(str(x) for x in field), 2)
        else:
            res = int("".join(str(x) for x in field), 2)
        return res