class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        hash_set = set(nums)
        longest = 0

        for i in hash_set:
            if i - 1 not in hash_set:
                current = i
                length = 1

                while current + 1 in hash_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest