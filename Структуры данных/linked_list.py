from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterator, TypeVar, final

T = TypeVar('T')


@final
@dataclass(slots=True, kw_only=True)
class Node(Generic[T]):
    value: T
    next: Node[T] | None = None


@final
@dataclass(slots=True, kw_only=True)
class LinkedList(Generic[T]):
    head: Node[T] | None = None
    
    def push_back(self, *, value: T) -> None:
        new_node = Node[T](value=value, next=None)
        if self.head is None:
            self.head = new_node
            return 
        
        current = self.head
        while current.next:
            current = current.next
            
        current.next = new_node
        
    def push_front(self, *, value: T) -> None:
        self.head = Node(value=value, next=self.head)
        
    def push_after_value(self, *, target_value: T, value: T) -> None:
        if self.head is None:
            return 
        
        new_node = Node[T](value=value, next=None)
        current = self.head
        while current:
            if current.value == target_value:
                new_node.next = current.next
                current.next = new_node
                return 
            current = current.next
            
    def push_before_value(self, *, target_value: T, value: T) -> None:
        if self.head is None:
            return 
        
        new_node = Node[T](value=value, next=None)
        if self.head.value == target_value:
            new_node.next = self.head
            self.head = new_node
            return 
        
        current = self.head
        while current.next:
            if current.next.value == target_value:
                new_node.next = current.next
                current.next = new_node
                return 
            current = current.next
            
    def remove_front(self) -> None:
        if self.head is None:
            return 
        self.head = self.head.next
    
    def remove_back(self) -> None:
        if self.head is None:
            return
         
        if self.head.next is None:
            self.head = None
            return
    
        current = self.head
        while current.next:
            if current.next.next is None:
                current.next = None
                return 
            current = current.next
    
    def remove(self, *, target_value: T) -> None:
        if self.head is None:
            return 
        
        if self.head.value == target_value:
            self.head = self.head.next
            return 
        
        current = self.head
        while current.next:
            if current.next.value == target_value:
                current.next = current.next.next
                return
            current = current.next
       
    def __iter__(self) -> Iterator[T]:
        current = self.head
        while current:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count
    
    def is_empty(self) -> bool:
        return self.head is None
    
    def __contains__(self, value: T) -> bool:
        return any(v == value for v in self)

#####################################################################
    
def test_push_back():
    ll = LinkedList[int]()
    ll.push_back(value=1)
    ll.push_back(value=2)
    ll.push_back(value=3)

    assert list(ll) == [1, 2, 3]
    assert len(ll) == 3


def test_push_front():
    ll = LinkedList[int]()
    ll.push_front(value=1)
    ll.push_front(value=2)
    ll.push_front(value=3)

    assert list(ll) == [3, 2, 1]
    assert len(ll) == 3


def test_push_after_value():
    ll = LinkedList[int]()
    for i in [1, 2, 4]:
        ll.push_back(value=i)

    ll.push_after_value(target_value=2, value=3)

    assert list(ll) == [1, 2, 3, 4]


def test_push_before_value():
    ll = LinkedList[int]()
    for i in [1, 3, 4]:
        ll.push_back(value=i)

    ll.push_before_value(target_value=3, value=2)

    assert list(ll) == [1, 2, 3, 4]


def test_remove_front():
    ll = LinkedList[int]()
    for i in [1, 2, 3]:
        ll.push_back(value=i)

    ll.remove_front()

    assert list(ll) == [2, 3]


def test_remove_back():
    ll = LinkedList[int]()
    for i in [1, 2, 3]:
        ll.push_back(value=i)

    ll.remove_back()

    assert list(ll) == [1, 2]


def test_remove():
    ll = LinkedList[int]()
    for i in [1, 2, 3, 4]:
        ll.push_back(value=i)

    ll.remove(target_value=3)

    assert list(ll) == [1, 2, 4]


def test_contains():
    ll = LinkedList[int]()
    for i in [1, 2, 3]:
        ll.push_back(value=i)

    assert 2 in ll
    assert 5 not in ll


def test_is_empty():
    ll = LinkedList[int]()
    assert ll.is_empty()

    ll.push_back(value=1)
    assert not ll.is_empty()


def test_len():
    ll = LinkedList[int]()
    assert len(ll) == 0

    ll.push_back(value=1)
    ll.push_back(value=2)

    assert len(ll) == 2


def test_edge_cases():
    ll = LinkedList[int]()

    ll.remove(target_value=1)
    ll.remove_front()
    ll.remove_back()

    assert list(ll) == []

    ll.push_after_value(target_value=1, value=2)
    ll.push_before_value(target_value=1, value=2)

    assert list(ll) == []

    ll.push_back(value=10)
    ll.remove_back()

    assert ll.is_empty()


if __name__ == "__main__":
    test_push_back()
    test_push_front()
    test_push_after_value()
    test_push_before_value()
    test_remove_front()
    test_remove_back()
    test_remove()
    test_contains()
    test_is_empty()
    test_len()
    test_edge_cases()
    print("Все тесты прошли успешно!")