class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        memo = [0 for x in range(len(gas))]
        
        def dive(station, my_gas, steps_left) -> bool:
            
            if station >= len(gas):
                station = 0
            
            if steps_left == 0:
                return True
        
            if my_gas >= memo[station]:
                if dive(station + 1, my_gas + gas[station] - cost[station], steps_left - 1) == False:
                    memo[station] = max(my_gas, memo[station])
                else: 
                    return True
            
            return False

        for i in range(len(gas)):
            if gas[i] > memo[i]:
                if dive(i + 1, gas[i] - cost[i], len(gas)):
                    return i
                else:
                    memo[i] =  max(0, memo[i])
        return -1