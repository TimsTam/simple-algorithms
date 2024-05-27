# Locates the maximum value a list of 'nums' using a recursive approach.

nums = [23, 34, 43, 12, 11, 23]


def maxValue(length, maximum):
    # len = the current index being processed
    # max = the maximum value found so far
    if maximum < nums[length]:
        maximum = nums[length]
    if length < 0:
        return maximum
    else:
        return maxValue(length - 1, maximum)


print(maxValue(len(nums) - 1, 0))
