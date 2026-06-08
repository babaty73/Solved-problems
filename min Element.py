#LeetCode problem 3300. Minimum Element
class Solution:
    def minElement(self, nums):
        digit_sums = []

        for num in nums:
            total = 0

            for digit in str(num):
                total += int(digit)

            digit_sums.append(total)

        return min(digit_sums)