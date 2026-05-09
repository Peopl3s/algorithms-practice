from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, TypeVar, final

T = TypeVar('T')


@final
@dataclass(slots=True, kw_only=True)
class DynamicArray(Generic[T]):
    _data: list[T | None] = field(init=False)
    _size: int = field(default=0, init=False)
    _capacity: int = field(default=4, init=False)

    def __post_init__(self):
        self._data = [None] * self._capacity
    
    def push_front(self, *, value: T) -> None:
        if self._size == self._capacity:
            self._grow()
        index = self._size
        while index > 0:
            self._data[index] = self._data[index - 1]
            index -= 1
        self._data[0] = value
        self._size += 1
    
    def push_back(self, *, value: T) -> None:
        if self._size == self._capacity:
            self._grow()
        self._data[self._size] = value
        self._size += 1
    
    def _grow(self) -> None:
        new_capacity = max(4, self._capacity * 2)
        new_data = [0] * new_capacity
        new_data[:self._size] = self._data[:self._size]
        self._data = new_data
        self._capacity = new_capacity
        
    def pop_front(self) -> None:
        if self._size == 0:
            return 
        for i in range(self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        
    def pop_back(self) -> None:
        if self._size == 0:
            return 
        self._size -= 1
        self._data[self._size] = None
    
    def front(self) -> T | None:
        if self._size == 0:
            return 
        return self._data[0]
    
    def back(self) -> T | None:
        if self._size == 0:
            return 
        return self._data[self._size - 1]
    
    def at(self, index: int) -> T | None:
        if index < 0 or index >= self._size:
            return 
        return self._data[index]
    
    def size(self) -> int:
        return self._size
    
    def capacity(self) -> int:
        return self._capacity
    
    
###############################################################

def main():
    arr = DynamicArray[int]()

    assert arr.size() == 0
    assert arr.capacity() == 4
    assert arr.front() is None
    assert arr.back() is None

    arr.push_back(value=10)
    arr.push_back(value=20)

    assert arr.size() == 2
    assert arr.front() == 10
    assert arr.back() == 20
    assert arr.at(0) == 10
    assert arr.at(1) == 20

    arr.push_front(value=5)

    assert arr.size() == 3
    assert arr.front() == 5
    assert arr.back() == 20
    assert arr.at(1) == 10

    arr.pop_back()

    assert arr.size() == 2
    assert arr.back() == 10

    arr.pop_front()

    assert arr.size() == 1
    assert arr.front() == 10
    assert arr.back() == 10

    arr.push_back(value=30)
    arr.push_back(value=40)
    arr.push_back(value=50)

    assert arr.size() == 4
    assert arr.capacity() >= 4

    arr.push_back(value=60)

    assert arr.size() == 5
    assert arr.capacity() == 8

    assert arr.at(-1) is None
    assert arr.at(100) is None

    print("All tests passed!")


if __name__ == "__main__":
    main()