'''
利用python列表的切片方法将元素从新排序
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:]+nums[0:n-k]


 '''
记录最后一个元素，将其弹出，再插入到列表最前面
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            a = nums[len(nums)-1]
            nums.pop()
            nums.insert(0,a)
'''