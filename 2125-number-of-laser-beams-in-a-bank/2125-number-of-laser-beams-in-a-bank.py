class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        summ = 0
        prev = 0
        for line in bank:
            cntline = 0
            for pr in line:
                if pr == '1':
                    cntline+=1
            if cntline > 0:
                summ += prev*cntline
                prev=cntline
        return summ
                    