from typing import List, Tuple


def twoSum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_and_index = {}
    for num1_index, num1 in enumerate(nums):
        num2 = target - num1
        try:
            num2_index = num_and_index[num2]
        except KeyError:
            num_and_index[num1] = num1_index
        else:
            return tuple(sorted([num1_index, num2_index]))


nums = [3, 2, 4]
target = 6


print(twoSum(nums, target))
