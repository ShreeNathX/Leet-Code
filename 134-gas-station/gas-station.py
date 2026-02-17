class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        index = tank = total = 0
        for i in range(len(cost)):
            x = gas[i] - cost[i]
            total += x
            tank += x

            if tank <0:
                index = i+1
                tank = 0
        if total>=0:
            return index
        else:
            return -1
