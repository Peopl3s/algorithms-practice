from typing import List

''' optimize 
reduce the inner loop segment by 1, after each full pass of the outer loop,
since the first full pass of the loop through the array the largest element
will pop up (move to the end of the array). The second largest element will 
pop up to the penultimate cell during the second loop pass, etc.
'''
def bubble_sort(arr: List[int]) -> None:
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# forehead
def bubble_sort_forehead(arr: List[int]) -> None:
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    arr = [5, 2, 6, 1, 0]
    bubble_sort(arr)
    print(arr)