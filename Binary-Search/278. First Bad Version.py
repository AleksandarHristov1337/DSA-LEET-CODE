# Brute Force - linear search
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        for x in range(1, n + 1):
            if isBadVersion(x):
                return x

# Binary Search
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2

            if isBadVersion(mid):  # check if mid satisfies condition
                # move left to find earlier occurrence
                high = mid
            else:
                # move right if mid does not satisfy condition
                low = mid + 1

        # After loop, low is the first "bad" version
        return low


# Knowing the  n versions [1, 2, ..., n] are sorted we can basically use Binary Search without worrying about randomness