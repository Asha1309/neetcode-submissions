class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count={}
        for i in nums:
            count[i]=1+count.get(i,0)
        return sorted(nums, key=lambda x: (count[x], -x))

        