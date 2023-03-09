# Python program for implementation of MergeSort
import random


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        lt = nums[:mid]
        rt = nums[mid:]
        merge_sort(lt)
        merge_sort(rt)
        i = j = k = 0
        while i < len(lt) and j < len(rt):
            if lt[i] <= rt[j]:
                nums[k] = lt[i]
                i += 1
            else:
                nums[k] = rt[j]
                j += 1
            k += 1
        while i < len(lt):
            nums[k] = lt[i]
            i += 1
            k += 1
        while j < len(rt):
            nums[k] = rt[j]
            j += 1
            k += 1


numbers = [random.randint(1, 1000) for x in range(1, 20)]
print(f'Unsorted list: {numbers}')
merge_sort(numbers)
print(f'Sorted list: {numbers}')
