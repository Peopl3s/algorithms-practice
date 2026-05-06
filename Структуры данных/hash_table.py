from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, Hashable, TypeVar, final

T = TypeVar('T', bound=Hashable)
V = TypeVar('V')

@final
@dataclass(slots=True, kw_only=True)
class Node(Generic[T, V]):
    key: T
    value: V
    next: Node[T, V] | None = None
    

@final
@dataclass(slots=True, kw_only=True)
class HashTable(Generic[T, V]):
    _data: list[Node[T, V] | None] = field(init=False)
    _capacity: int = field(default=4)
    _size: int = field(default=0)
    _load_factor_threshold: float = field(default=0.7)
    
    def __post_init__(self) -> None:
        self._data = [None] * self._capacity
        
    def insert(self, *, key: T, value: V) -> None:
        if (self._size + 1) / self._capacity > self._load_factor_threshold:
            self.rehash()
            
        index = self._hash(key=key)
        node = self._data[index]
        
        while node is not None:
            if node.key == key:
                node.value = value
                return 
            node = node.next
        
        new_node = Node[T, V](
            key=key, 
            value=value, 
            next=self._data[index],
        )
        self._data[index] = new_node
        self._size += 1
        
    def rehash(self) -> None:
        old_data = self._data
        old_capacity = self._capacity
        
        new_capacity = old_capacity * 2
        self._data = [None] * new_capacity
        self._capacity = new_capacity
        self._size = 0
        
        for i in range(0, old_capacity):
            current = old_data[i]
            while current is not None:
                self.insert(key=current.key, value=current.value)
                current = current.next
    
    def erase(self, *, key: T) -> None:
        index = self._hash(key=key)
        head = self._data[index]
        if head is None:
            return 
        
        if head.key == key:
            self._data[index] = head.next
            self._size -= 1
            return 
        
        prev = head
        current = head.next
        
        while current is not None:
            if current.key == key:
                prev.next = current.next
                self._size -= 1
                return 
            prev = current
            current = current.next
    
    def get(self, *, key: T) -> V | None:
        index = self._hash(key=key)
        node = self._data[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
    
    def size(self) -> int:
        return  self._size
    
    def _hash(self, *, key: T) -> int:
        return hash(key) & (self._capacity - 1)    
    
#################################################################

def test_insert_and_get():
    ht = HashTable[int, str]()
    
    ht.insert(key=1, value="one")
    ht.insert(key=2, value="two")
    
    assert ht.get(key=1) == "one"
    assert ht.get(key=2) == "two"
    assert ht.get(key=3) is None


def test_update_value():
    ht = HashTable[int, str]()
    
    ht.insert(key=1, value="one")
    ht.insert(key=1, value="ONE")
    
    assert ht.get(key=1) == "ONE"
    assert ht.size() == 1


def test_collision_handling():
    ht = HashTable[int, str](_capacity=4)
    
    keys = [0, 4, 8]
    
    for i, k in enumerate(keys):
        ht.insert(key=k, value=str(i))
    
    for i, k in enumerate(keys):
        assert ht.get(key=k) == str(i)
    
    assert ht.size() == 3


def test_erase():
    ht = HashTable[int, str]()
    
    ht.insert(key=1, value="one")
    ht.insert(key=2, value="two")
    
    ht.erase(key=1)
    
    assert ht.get(key=1) is None
    assert ht.get(key=2) == "two"
    assert ht.size() == 1


def test_erase_in_chain():
    ht = HashTable[int, str](_capacity=4)
    
    keys = [0, 4, 8]
    for i, k in enumerate(keys):
        ht.insert(key=k, value=str(i))
    
    ht.erase(key=4)
    
    assert ht.get(key=4) is None
    assert ht.get(key=0) == "0"
    assert ht.get(key=8) == "2"
    assert ht.size() == 2


def test_rehash():
    ht = HashTable[int, str](_capacity=2, _load_factor_threshold=0.5)
    
    ht.insert(key=1, value="one")
    ht.insert(key=2, value="two")
    
    assert ht._capacity >= 4
    assert ht.get(key=1) == "one"
    assert ht.get(key=2) == "two"
    assert ht.size() == 2


def main():
    test_insert_and_get()
    test_update_value()
    test_collision_handling()
    test_erase()
    test_erase_in_chain()
    test_rehash()
    
    print("Все тесты пройдены!")


if __name__ == "__main__":
    main()