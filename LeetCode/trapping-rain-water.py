class Solution(object):
    def trap(self, elevation):
        if len(elevation)  < 3:
            return 0
        front, frontMax, back, backMax = 0, 0, len(elevation) - 1, 0
        totalRain = 0
        while front < back:
            frontMax, backMax = max(frontMax, elevation[front]), max(backMax, elevation[back])
            if frontMax < backMax:
                totalRain += frontMax - elevation[front]
                front += 1
            else:
                totalRain += backMax - elevation[back]
                back -= 1
        return totalRain