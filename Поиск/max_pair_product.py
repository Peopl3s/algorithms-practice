from typing import Sequence, Tuple, MutableSequence

def max_pair_product(nums: Sequence[int]) -> int:
    max_num1, seq = max_tournament(0, len(nums) - 1, nums)
    max_num2 = max_tournament(0, len(seq) - 1, seq)[0]
    return (max_num1 * max_num2)

# https://users.csc.calpoly.edu/~dekhtyar/349-Fall2017/lectures/lec03.349.pdf  
def max_tournament(lo: int, hi: int, seq: Sequence[int]) -> Tuple[int, MutableSequence[int]]:
    if lo >= hi:
        return seq[lo], []
    mid = lo + (hi - lo) // 2
    value1, seq1 = max_tournament(lo, mid, seq)
    value2, seq2 = max_tournament(mid + 1, hi, seq)

    if value1 > value2:
        seq1.append(value2)
        return value1, seq1
    seq2.append(value1)
    return value2, seq2

def max_pair_product_line(nums: Sequence[int]) -> int:
    index = 0 
    for i in range(1, len(nums)):
        if nums[i] > nums[index]:
            index = i
    nums[index], nums[len(nums) - 1] = nums[len(nums) - 1], nums[index]
    index = 0
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[index]:
            index = i
    nums[index], nums[len(nums) - 2] = nums[len(nums) - 2], nums[index]
    return  nums[len(nums) - 2] * nums[len(nums) - 1]

if __name__ == '__main__':
    arr = [1, 3, 7, 2, 9]
    print(max_pair_product(arr))
    print(max_pair_product_line(arr))