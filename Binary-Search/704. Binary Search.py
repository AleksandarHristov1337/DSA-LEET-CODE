# Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # We set two variables for the list length: 0 is the start and len(nums) - 1 is the end
        low = 0
        high = len(nums) - 1

        # Here we check if high is bigger than low; if it is, it means the list is not empty
        while low <= high:
            # Here we get the middle index using // which basically rounds down
            # So if we have 7 elements, we have 3 as the middle
            mid = (low + high) // 2

            # This basically checks if we have found the target;
            # if we haven't, we continue searching left or right
            guess = nums[mid]

            # If we get a match of the target and guess, we return index
            if guess == target:
                return mid
            # If the target is bigger than the guess (e.g., at index 3), 
            # we set low = mid + 1 and continue
            elif guess < target:
                low = mid + 1
            # If the target is smaller than the guess (e.g., at index 3),
            # we set high = mid - 1 and continue
            else:
                high = mid - 1

        return -1
