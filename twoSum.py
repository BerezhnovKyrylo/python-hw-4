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
#twoSum([3, 3], 6)           # [0, 1]

def twoSum(num, target):
    dict = {}
    for i in range(len(num)):
        if num[i] not in dict:
            dict[target - num[i]] = i
        else:
            return [dict[num[i]], i]
    return [-1, -1]



print(twoSum([3, 2, 4], 6))
