class Solution:
    def dailyTemperatures(self, tem: List[int]) -> List[int]:
        
        dist = [0 for i in range(len(tem))]
        
        for i in reversed(range(len(tem))):
            j = i + 1
            while j < len(tem) and tem[j] <= tem[i]:
                if (dist[j] > 0):
                    j += dist[j]
                else:
                    j = len(tem)
            if j < len(tem): 
                dist[i] = j - i
                
        return dist    
