class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        remaining_gas = 0
        start_index = 0
        for i in range(n):
            remaining_gas += gas[i] - cost[i]
            if remaining_gas < 0:
                start_index = i + 1
                remaining_gas = 0
        if sum(gas) < sum(cost):
            return -1
        return start_index

