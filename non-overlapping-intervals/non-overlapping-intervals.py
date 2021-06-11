class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def lexi(lst):
            return lst[0]*2001+2000-lst[1] # return 1-4 1-3 1-2 2-8 2-5 2-1
        
        intervals = [x for x in sorted(intervals, key = lexi)]
        prevEnding = -2001
        counter = 0
        for inter in intervals:
            if inter[0] < prevEnding:
                counter += 1
                prevEnding = min(prevEnding, inter[1])
            else:
                prevEnding = inter[1]
        return counter