class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        hl, hr = [height[0]], [height[-1]]

        for i in range(1,len(height)):
            if hl[i-1] < height[i]:
                hl.append(height[i])
            else:
                hl.append(hl[i-1])
        
        for i in range(len(height) -2, -1, -1 ):
            if hr[len(height) - i -2] <  height[i]:
                hr.append(height[i])
            else:
                hr.append(hr[len(height) - i - 2])
        
        hr = hr[::-1]
        trapped = 0
        for i in range(len(height)):
            trapped += ((min(hl[i] , hr[i])) - height[i])

        return trapped