class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        sorted_count = sorted(
            count.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [num for num, frequency in sorted_count[:k]]

        