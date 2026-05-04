from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterator, TypeVar, final

T = TypeVar('T')


@final
@dataclass(slots=True, kw_only=True)
class Node(Generic[T]):
    value: T
    next: Node[T] | None = None
    prev: Node[T] | None = None


@final
@dataclass(slots=True, kw_only=True)
class DoubleLinkedList(Generic[T]):
    head: Node[T] | None = None
    tail: Node[T] | None = None

    def push_back(self, *, value: T) -> None:
        new_node = Node(value=value)

        if self.tail is None:
            self.head = self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def push_front(self, *, value: T) -> None:
        new_node = Node(value=value)

        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def push_after_value(self, *, target_value: T, value: T) -> None:
        current = self.head

        while current:
            if current.value == target_value:
                new_node = Node(value=value)

                new_node.next = current.next
                new_node.prev = current

                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node

                current.next = new_node
                return

            current = current.next

    def push_before_value(self, *, target_value: T, value: T) -> None:
        current = self.head

        while current:
            if current.value == target_value:
                new_node = Node(value=value)

                new_node.prev = current.prev
                new_node.next = current

                if current.prev:
                    current.prev.next = new_node
                else:
                    self.head = new_node

                current.prev = new_node
                return

            current = current.next

    def remove_front(self) -> None:
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def remove_back(self) -> None:
        if self.tail is None:
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None

    def remove(self, *, target_value: T) -> None:
        current = self.head

        while current:
            if current.value == target_value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

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

#################################################################################
def assert_integrity(ll: DoubleLinkedList[int]) -> None:
    current = ll.head
    prev = None

    while current:
        assert current.prev == prev
        prev = current
        current = current.next

    if prev is None:
        assert ll.tail is None
    else:
        assert ll.tail == prev


def test_push_back():
    ll = DoubleLinkedList[int]()
    ll.push_back(value=1)
    ll.push_back(value=2)
    ll.push_back(value=3)

    assert list(ll) == [1, 2, 3]
    assert len(ll) == 3
    assert ll.tail.value == 3
    assert_integrity(ll)


def test_push_front():
    ll = DoubleLinkedList[int]()
    ll.push_front(value=1)
    ll.push_front(value=2)
    ll.push_front(value=3)

    assert list(ll) == [3, 2, 1]
    assert ll.head.value == 3
    assert ll.tail.value == 1
    assert_integrity(ll)


def test_push_after_value():
    ll = DoubleLinkedList[int]()
    for i in [1, 2, 4]:
        ll.push_back(value=i)

    ll.push_after_value(target_value=2, value=3)

    assert list(ll) == [1, 2, 3, 4]
    assert_integrity(ll)


def test_push_before_value():
    ll = DoubleLinkedList[int]()
    for i in [1, 3, 4]:
        ll.push_back(value=i)

    ll.push_before_value(target_value=3, value=2)

    assert list(ll) == [1, 2, 3, 4]
    assert_integrity(ll)


def test_remove_front():
    ll = DoubleLinkedList[int]()
    for i in [1, 2, 3]:
        ll.push_back(value=i)

    ll.remove_front()

    assert list(ll) == [2, 3]
    assert ll.head.prev is None
    assert_integrity(ll)


def test_remove_back():
    ll = DoubleLinkedList[int]()
    for i in [1, 2, 3]:
        ll.push_back(value=i)

    ll.remove_back()

    assert list(ll) == [1, 2]
    assert ll.tail.next is None
    assert_integrity(ll)


def test_remove():
    ll = DoubleLinkedList[int]()
    for i in [1, 2, 3, 4]:
        ll.push_back(value=i)

    ll.remove(target_value=3)

    assert list(ll) == [1, 2, 4]
    assert_integrity(ll)


def test_remove_head():
    ll = DoubleLinkedList[int]()
    for i in [1, 2, 3]:
        ll.push_back(value=i)

    ll.remove(target_value=1)

    assert list(ll) == [2, 3]
    assert ll.head.prev is None
    assert_integrity(ll)


def test_remove_tail():
    ll = DoubleLinkedList[int]()
    for i in [1, 2, 3]:
        ll.push_back(value=i)

    ll.remove(target_value=3)

    assert list(ll) == [1, 2]
    assert ll.tail.next is None
    assert_integrity(ll)


def test_contains():
    ll = DoubleLinkedList[int]()
    for i in [1, 2, 3]:
        ll.push_back(value=i)

    assert 2 in ll
    assert 5 not in ll


def test_is_empty():
    ll = DoubleLinkedList[int]()
    assert ll.is_empty()

    ll.push_back(value=1)
    assert not ll.is_empty()


def test_len():
    ll = DoubleLinkedList[int]()
    assert len(ll) == 0

    ll.push_back(value=1)
    ll.push_back(value=2)

    assert len(ll) == 2


def test_edge_cases():
    ll = DoubleLinkedList[int]()

    ll.remove(target_value=1)
    ll.remove_front()
    ll.remove_back()

    assert list(ll) == []
    assert ll.head is None and ll.tail is None

    ll.push_after_value(target_value=1, value=2)
    ll.push_before_value(target_value=1, value=2)

    assert list(ll) == []

    ll.push_back(value=10)
    ll.remove_back()

    assert ll.is_empty()
    assert ll.head is None and ll.tail is None


if __name__ == "__main__":
    test_push_back()
    test_push_front()
    test_push_after_value()
    test_push_before_value()
    test_remove_front()
    test_remove_back()
    test_remove()
    test_remove_head()
    test_remove_tail()
    test_contains()
    test_is_empty()
    test_len()
    test_edge_cases()
    print("Все тесты для двусвязного списка прошли успешно!")
    