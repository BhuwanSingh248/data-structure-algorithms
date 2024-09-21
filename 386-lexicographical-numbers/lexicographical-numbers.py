class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # return sorted([i for i in range(1, n+1)], key=str)
        result = []
        def helper(num):
            if num > n:
                return 
            
            result.append(num)

            for i in range(10):
                next_num = num * 10 + i
                if next_num > n:
                    return 
                helper(next_num)

            
        for i in range(1, 10):
            if i > n:
                break 
            helper(i)
        return result