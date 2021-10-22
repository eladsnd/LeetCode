"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


# Sol if the array is sorted
def two_sorted_Sum(self, nums: List[int], target: int) -> List[int]:
    """
    :param self:
    :param nums: a list of numbers
    :param target: target number witch is reachable
    :return: numbers locations
    """
    e = len(nums)
    s = 0
    while e > s:
        if nums[s] + nums[e] > target:
            e -= 1
        elif e < s:
            s += 1
        else:
            break
    return [s, e]


def tow_sum(nums: List[int], target: int) -> List[int]:
    target_dir = {}
    for i in range(len(nums)):
        if nums[i] in target_dir:
            return [target_dir[nums[i]], i]
        else:
            target_dir[target - nums[i]] = i


if __name__ == '__main__':
    print(tow_sum([2, 7, 11, 15], 9))
