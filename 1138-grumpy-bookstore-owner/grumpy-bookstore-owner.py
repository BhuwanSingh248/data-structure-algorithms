class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        int_sat = 0
        max_extra_sat = 0
        curr_window_sat = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                int_sat += customers[i]
            
            elif i < minutes:
                curr_window_sat += customers[i]
        
        max_extra_sat = curr_window_sat

        for i in range(minutes, len(customers)):
            curr_window_sat += customers[i] * grumpy[i]
            curr_window_sat -= customers[i-minutes] * grumpy[i-minutes]
            max_extra_sat = max(max_extra_sat, curr_window_sat)
        
        return int_sat + max_extra_sat