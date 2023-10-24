from typing import List

def recursive_binary_search(arr: List[int], start: int, end: int, target: int) -> int:
    if start > end:
        return -1
    # (start + end) - maight overflow
    # works with pointers too
    mid = start + (end - start) // 2
    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        return recursive_binary_search(arr, start, mid - 1, target)
    if target > arr[mid]:
        return recursive_binary_search(arr, mid + 1, end, target)


def iterative_binary_search(arr: List[int], target: int) -> int:
    start = 0
    end = len(arr) - 1 
    while(start <= end):
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            end = mid - 1 
        elif target > arr[mid]:
            start = mid + 1 
    return -1


if __name__ == '__main__':
    arr = [5, 2, 6, 1, 0]
    target = 5
    sorted_arr = sorted(arr)
    print(sorted_arr)
    print(recursive_binary_search(sorted_arr, 0, len(sorted_arr) - 1, target))
    print(iterative_binary_search(sorted_arr, target))