'''
Runtime: 28 ms, faster than 90.41% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 14.1 MB, less than 87.60% of Python3 online submissions for Number of Good Pairs.
'''
class Solution:
    # Remove the first element and compare with rest of the elements
    # Increment the good_pairs count for each match
    # Repeat for the next element
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        for i in range(len(nums)):
            var1 = nums.pop(0)
            for num in nums:
                if var1 == num:
                    good_pairs += 1
        return good_pairs
