class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: # nums = list of integers, val = integer, returns integer denoting the number of elements in list
        count = nums.count(val)                                # counts the val in the numsList
        for i in range(count):
            nums.remove(val)                                   # removes first occurence of val
        return len(nums)                                       # returns modified numsList
