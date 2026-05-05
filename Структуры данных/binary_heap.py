from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, TypeVar, final

T = TypeVar('T')


@final
@dataclass(slots=True, kw_only=True)
class BinaryHeap(Generic[T]):
    _data: list[T] = field(default_factory=list)
    
    def insert(self, *, value: T) -> None:
        self._data.append(value)
        self.sift_up(index=(len(self._data) - 1))
        
    def sift_up(self, *, index: int) -> None:
        while index > 0:
            parent_index = (index - 1) // 2
            if self._data[index] > self._data[parent_index]:
                self._data[index], self._data[parent_index] = self._data[parent_index], self._data[index]
                index = parent_index
            else:
                break
    
    def erase_max(self) -> None:
        if len(self._data) == 0:
            return 
        
        self._data[0] = self._data[len(self._data) - 1]
        self._data = self._data[:len(self._data) - 1]
        
        if len(self._data) != 0:
            self.sift_down(index=0)
    
    def sift_down(self, *, index: int) -> None:
        while True:
            left_child_idx = 2 * index + 1
            right_child_idx = 2 * index + 2
            largest_idx = index

            if (
                left_child_idx < len(self._data) 
                and self._data[left_child_idx] > self._data[largest_idx]
            ):
                largest_idx = left_child_idx

            if (
                right_child_idx < len(self._data) 
                and self._data[right_child_idx] > self._data[largest_idx]
            ):
                largest_idx = right_child_idx

            if largest_idx != index:
                self._data[index], self._data[largest_idx] = self._data[largest_idx], self._data[index]
                index = largest_idx
            else:
                break
            
    def max(self) -> T | None:
        if len(self._data) == 0:
            return 
        
        return self._data[0]
    
    def size(self) -> int:
        return len(self._data)
    
    
#######################################################

def test_empty_heap():
    heap = BinaryHeap[int]()
    assert heap.size() == 0
    assert heap.max() is None


def test_single_insert():
    heap = BinaryHeap[int]()
    heap.insert(value=10)
    
    assert heap.size() == 1
    assert heap.max() == 10


def test_multiple_inserts():
    heap = BinaryHeap[int]()
    heap.insert(value=5)
    heap.insert(value=10)
    heap.insert(value=3)
    
    assert heap.size() == 3
    assert heap.max() == 10


def test_heap_property_after_inserts():
    heap = BinaryHeap[int]()
    values = [3, 1, 6, 5, 2, 4]
    
    for v in values:
        heap.insert(value=v)
    
    assert heap.max() == 6


def test_erase_max():
    heap = BinaryHeap[int]()
    values = [3, 1, 6, 5, 2, 4]
    
    for v in values:
        heap.insert(value=v)
    
    heap.erase_max()
    assert heap.max() == 5

    heap.erase_max()
    assert heap.max() == 4


def test_erase_until_empty():
    heap = BinaryHeap[int]()
    values = [1, 2, 3]
    
    for v in values:
        heap.insert(value=v)
    
    heap.erase_max()
    heap.erase_max()
    heap.erase_max()
    
    assert heap.size() == 0
    assert heap.max() is None


def test_sorted_order_extraction():
    heap = BinaryHeap[int]()
    values = [4, 1, 7, 3, 8, 5]
    
    for v in values:
        heap.insert(value=v)
    
    result = []
    while heap.size() > 0:
        result.append(heap.max())
        heap.erase_max()
    
    assert result == sorted(values, reverse=True)


def test_duplicate_values():
    heap = BinaryHeap[int]()
    values = [5, 5, 5]
    
    for v in values:
        heap.insert(value=v)
    
    assert heap.max() == 5
    
    heap.erase_max()
    assert heap.max() == 5


def test_negative_values():
    heap = BinaryHeap[int]()
    values = [-1, -5, -3]
    
    for v in values:
        heap.insert(value=v)
    
    assert heap.max() == -1


def run_all_tests():
    test_empty_heap()
    test_single_insert()
    test_multiple_inserts()
    test_heap_property_after_inserts()
    test_erase_max()
    test_erase_until_empty()
    test_sorted_order_extraction()
    test_duplicate_values()
    test_negative_values()
    print("Все тесты пройдены!")


if __name__ == "__main__":
    run_all_tests()
