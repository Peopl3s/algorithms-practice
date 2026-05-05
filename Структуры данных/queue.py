from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar, final

T = TypeVar('T')


@final
@dataclass(slots=True, kw_only=True)
class Node(Generic[T]):
    value: T
    next: Node[T] | None = None


@final
@dataclass(slots=True, kw_only=True)
class Queue(Generic[T]):
    head: Node[T] | None = None
    tail: Node[T] | None = None
    
    def push(self, *, value: T) -> None:
        new_node = Node[T](value=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def pop(self) -> T | None:
        if self.head is None:
            return 
        
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value
            
    def front(self) -> T | None:
        if self.head is None:
            return 
        return self.head.value
    
    def back(self) -> T | None:
        if self.tail is None:
            return 
        return self.tail.value
    
    def size(self) -> int:
        if self.head is None:
            return 0
        
        size = 0
        current = self.head
        while current:
            size +=1
            current = current.next
        return size


######################################################################

def test_queue() -> None:
    q = Queue[int]()

    assert q.pop() is None
    assert q.front() is None
    assert q.back() is None
    assert q.size() == 0

    q.push(value=10)
    assert q.front() == 10
    assert q.back() == 10
    assert q.size() == 1

    assert q.pop() == 10
    assert q.pop() is None
    assert q.size() == 0

    q.push(value=1)
    q.push(value=2)
    q.push(value=3)

    assert q.front() == 1
    assert q.back() == 3
    assert q.size() == 3

    assert q.pop() == 1
    assert q.pop() == 2
    assert q.front() == 3
    assert q.back() == 3
    assert q.size() == 1

    assert q.pop() == 3
    assert q.pop() is None

    assert q.front() is None
    assert q.back() is None
    assert q.size() == 0

    q.push(value=42)
    assert q.front() == 42
    assert q.back() == 42
    assert q.size() == 1


if __name__ == "__main__":
    test_queue()
    print("Все тесты пройдены!")
    