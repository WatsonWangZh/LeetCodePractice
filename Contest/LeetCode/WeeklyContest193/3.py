# 5455. Minimum Number of Days to Make m Bouquets
# User Accepted:1394
# User Tried:3068
# Total Accepted:1442
# Total Submissions:6104
# Difficulty:Medium
# Given an integer array bloomDay, an integer m and an integer k.
# We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

# Example 1:
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let's see what happened in the first three days.
# x means flower bloomed and _ means flower didn't bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

# Example 2:
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
# Output: -1
# Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers.
# We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.

# Example 3:
# Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
# Output: 12
# Explanation: We need 2 bouquets each should have 3 flowers.
# Here's the garden after the 7 and 12 days:
# After day 7: [x, x, x, x, _, x, x]
# We can make one bouquet of the first three flowers that bloomed.
# We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
# After day 12: [x, x, x, x, x, x, x]
# It is obvious that we can make two bouquets in different ways.

# Example 4:
# Input: bloomDay = [1000000000,1000000000], m = 1, k = 1
# Output: 1000000000
# Explanation: You need to wait 1000000000 days to have a flower ready for a bouquet.

# Example 5:
# Input: bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
# Output: 9
 
# Constraints:
# bloomDay.length == n
# 1 <= n <= 10^5
# 1 <= bloomDay[i] <= 10^9
# 1 <= m <= 10^6
# 1 <= k <= n

from collections import defaultdict
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        # 排序 贪心 TLE
        # if len(bloomDay) < m * k:
        #     return -1
        #
        # tmp = bloomDay[:]
        # sortedbloomDay = sorted(bloomDay)
        # if k == 1:
        #     return sortedbloomDay[m - 1]
        #
        # def check(lst, m, k, n):
        #     cnt = 0
        #     for i in range(len(lst)):
        #         if lst[i] <= m:
        #             cnt += 1
        #             if cnt >= k:
        #                 n -= 1
        #                 cnt -= k
        #         else:
        #             cnt = 0
        #
        #     if n == 0:
        #         return True
        #     return False
        #
        # for ele in sorted(tmp):
        #     if check(bloomDay, ele, k, m):
        #         return ele
        #
        # return -1

        # 动态维护区间
        def helper(l, r, k):
            return (r - l + 1) // k

        n = len(bloomDay)
        l, r = [0] * (n + 2), [0] * (n + 2)

        tmp = []
        for idx, day in enumerate(bloomDay):
            tmp.append([day, idx + 1])
        tmp.sort()

        curr_sum = 0
        for ele in tmp:
            i = ele[1]
            if l[i - 1] and r[i + 1]:
                curr_sum = curr_sum - helper(l[i - 1], i - 1, k) - helper(i + 1, r[i + 1], k) + helper(l[i - 1],
                                                                                                       r[i + 1], k)
                r[l[i - 1]] = r[i + 1]
                l[r[i + 1]] = l[i - 1]
            elif l[i - 1]:
                curr_sum = curr_sum - helper(l[i - 1], i - 1, k) + helper(l[i - 1], i, k)
                r[l[i - 1]] = i
                l[i] = l[i - 1]
            elif r[i + 1]:
                curr_sum = curr_sum - helper(i + 1, r[i + 1], k) + helper(i, r[i + 1], k)
                l[r[i + 1]] = i
                r[i] = r[i + 1]
            else:
                curr_sum = curr_sum + helper(i, i, k)
                r[i] = l[i] = i

            if curr_sum >= m:
                return ele[0]

        return -1