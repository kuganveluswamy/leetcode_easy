class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = abs(x)
        v = ''
        ns = str(n)
        for i in ns:
            v = i + v
        v = int(v)
        if ((2**31) - 1) > v > (-2**31):
            if x > 0:
                sign = 1
            else:
                sign = -1
        else:
            sign = 0
        return (sign * v)
