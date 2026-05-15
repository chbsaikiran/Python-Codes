class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            y = 0 - x
        else:
            y = x
        s = str(y)
        s = s[::-1]
        if x < 0:
            s = "-"+s

        z = int(s)
        if z > 2147483647 or z < -2147483648:
            return 0;
        return z
