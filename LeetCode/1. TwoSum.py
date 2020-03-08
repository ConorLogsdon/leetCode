class Solution:
    def twoSum(self, nums, target):
        map = {}
        
        for i, number in enumerate(nums):
            complement = target - number
            if complement in map:
                return (map[complement], i)
            map[number] = i
