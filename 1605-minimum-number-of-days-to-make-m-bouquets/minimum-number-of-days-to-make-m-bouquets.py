class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        n = len(bloomDay)

        def validDay(mid):
            cc, bq = 0, 0

            for i in range(n):
                if bloomDay[i] <= mid:
                    cc += 1
                else:
                    cc = 0
                
                if cc == k :
                    bq+=1
                    cc = 0
            return bq >= m
        
        l, r, ans = 1, max(bloomDay), -1

        while  l<=r:
            mid = (l+r) // 2
            if validDay(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans