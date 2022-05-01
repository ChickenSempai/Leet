class Solution:
    def earliestFullBloom(self, pT: List[int], gT: List[int]) -> int:
        nw = []
        for i in range(len(pT)):
            nw.append([gT[i], pT[i]])
        nw.sort(reverse=True)
        print(nw)
        for i in range(1, len(nw)):
            newpT= nw[i-1][1] + nw[i][1]
            nw[i][0]= min(max(nw[i][0], nw[i-1][0]-nw[i][1]), max(nw[i-1][0],nw[i][0]-nw[i-1][1]))
            nw[i][1] = newpT
        return nw[-1][1]+nw[-1][0]