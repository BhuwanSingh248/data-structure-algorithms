class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0 
        n = len(arr)

        for i in range(n):
            val = arr[i]

            for k in range(i+1, n):
                val ^= arr[k]

                if val == 0:
                    count += (k-i)
        return count