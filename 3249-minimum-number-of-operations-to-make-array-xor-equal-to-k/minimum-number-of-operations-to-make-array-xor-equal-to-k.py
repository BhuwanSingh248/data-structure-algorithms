class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0

        for n in nums:
            xor ^= n
        
        count = 0

        while k or xor:
            if k%2 != xor%2:
                count += 1
            
            k //= 2
            xor //= 2

        return count