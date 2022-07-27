#from typing import List

# Дано масив цілих чисел nums і ціле число,
# поверніть індекси двох чисел так, щоб їх сума дала передане ціле число.

# Ви можете припустити, що кожен вхід матиме рівно одне рішення,
# і ви не можете використовувати той самий елемент двічі.

# Ви можете повернути відповідь у будь-якому порядку.

#def twoSum(nums: List[int], target: int) -> List[int]:
#    print(nums, target)

#twoSum([1, 2, 3], 4)        # [0, 2]
#twoSum([2, 7, 11, 15], 9)   # [0, 1]
#twoSum([3, 2, 4], 6)        # [1, 2]
#twoSum([3, 3], 6)           # [0, 1]

from typing import List


<<<<<<< HEAD
def twoSum(nums: List[int], target: int):
=======
def twosum(nums: List[int], target: int):
>>>>>>> 63ca7a20e39a633490b0eb9b7ac4139620fc1494
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print([i, j])
                return


two_sum([1, 2, 3], 4)
two_sum([2, 7, 11, 15], 9)
two_sum([3, 2, 4], 6)
two_sum([3, 3], 6)
