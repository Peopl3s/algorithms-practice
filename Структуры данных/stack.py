from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, TypeVar, final

T = TypeVar('T')


@final
@dataclass(slots=True, kw_only=True)
class Stack(Generic[T]):
    _arr: list[T] = field(default_factory=list)
    
    def push(self, *, value: T) -> None:
        self._arr.append(value)
    
    def pop(self) -> T | None:
        if len(self._arr) == 0:
            return
        pop_item = self._arr[-1]
        self._arr = self._arr[:-1]
        return pop_item
    
    def top(self) -> T | None:
        if len(self._arr) == 0:
            return 
        return self._arr[-1]
    
    def size(self) -> int:
        return len(self._arr)

##########################################################

def test_stack():
    s = Stack[int]()

    assert s.size() == 0
    assert s.pop() is None
    assert s.top() is None

    s.push(value=10)
    assert s.size() == 1
    assert s.top() == 10

    s.push(value=20)
    s.push(value=30)
    assert s.size() == 3
    assert s.top() == 30

    assert s.pop() == 30
    assert s.size() == 2
    assert s.top() == 20

    assert s.pop() == 20
    assert s.pop() == 10

    assert s.size() == 0
    assert s.pop() is None
    assert s.top() is None


def test_stack_types():
    s = Stack[str]()

    s.push(value="a")
    s.push(value="b")

    assert s.top() == "b"
    assert s.pop() == "b"
    assert s.pop() == "a"
    assert s.pop() is None


def test_lifo_behavior():
    s = Stack[int]()

    for i in range(5):
        s.push(value=i)

    result = [s.pop() for _ in range(5)]
    assert result == [4, 3, 2, 1, 0]


if __name__ == "__main__":
    test_stack()
    test_stack_types()
    test_lifo_behavior()
    print("Все тесты пройдены!")
    