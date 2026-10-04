class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        deka = set()

        for num in nums:
            if num in deka:
                return True

            deka.add(num)
        return False