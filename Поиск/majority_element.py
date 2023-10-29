'''
Find the majority element (Boyer-Moore majority voting algorithm)

The majority element appears more than n/2 times, where n is the size of the array.
'''
from typing import List

def find_majority_element_naive(nums: List[int]) -> int:
    i = 0
    n = len(nums)
    while(n and i <= n // 2):
        count = 1
        for j in range(i + 1, n):
            if nums[j] == nums[i]:
                count +=1 
        if count > n // 2:
            return nums[i]
        i +=1
    return -1


def find_majority_element_faster(nums: List[int]):
    def _binsearch(arr: List[int], target: int) -> int:
        first_occurrence = -1
        last_occurrence = -1
        start = 0
        end = len(arr) - 1 
        while(start <= end):
            mid = start + (end - start) // 2
            if arr[mid] == target:
                first_occurrence = mid
                end = mid - 1
            elif target < arr[mid]:
                end = mid - 1 
            elif target > arr[mid]:
                start = mid + 1 
                
        start = 0
        end = len(arr) - 1
        while(start <= end):
            mid = start + (end - start) // 2
            if arr[mid] == target:
                last_occurrence = mid
                start = mid  + 1
            elif target < arr[mid]:
                end = mid - 1 
            elif target > arr[mid]:
                start = mid + 1 
        return first_occurrence, last_occurrence
        
    nums = sorted(nums)
    n = len(nums)
    for num in nums:
        first_occurrence, last_occurrence = _binsearch(nums, num)
        if (last_occurrence - first_occurrence) >= n // 2:
            return num
    return -1

def find_majority_element_map(nums: List[int]) -> int:
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1
 
    for key, value in d.items():
        if value > len(nums) // 2:
            return key
    return -1


def find_majority_element_boyer_moore(nums: List[int]) -> int:
    '''
    The Boyer-Moore voting algorithm gives correct results
    only when there is a majoritarian element in the input data.
    '''
    m = -1
    i = 0
    for j in range(len(nums)):
        if i == 0:
            m = nums[j]
            i = 1
        elif m == nums[j]:
            i = i + 1
        else:
            i = i - 1
    return m

if __name__ == '__main__':
    nums = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
    print(find_majority_element_naive(nums))
    print(find_majority_element_faster(nums))
    print(find_majority_element_map(nums))
    print(find_majority_element_boyer_moore(nums))
