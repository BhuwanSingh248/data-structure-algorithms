class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        temp = set(arr)
        curr = arr[0]
        nxt = arr[1]
        ans = 0
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                curr = arr[i]
                nxt = arr[j]
                tmp = 2
                while ((curr + nxt) in temp):
                    curr, nxt = nxt, curr+nxt
                    tmp += 1
                ans = max(ans, tmp) if tmp > 2 else ans
                
        return ans if ans else 0
            
