from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, TypeVar, final

T = TypeVar('T')


@final
@dataclass(slots=True, kw_only=True)
class TreeNode(Generic[T]):
    value: T
    left: TreeNode[T] | None = None
    right: TreeNode[T] | None = None


@final
@dataclass(slots=True, kw_only=True)
class BinarySearchTree (Generic[T]):
    _size: int = field(default=0)
    _root: TreeNode[T] | None = None
    
    def insert(self, *, value: T) -> None:
        self._root = self._insert_recursive(
            node=self._root, 
            value=value,
        )
        self._size += 1
    
    def _insert_recursive(
        self, 
        *, 
        node: TreeNode[T] | None, 
        value: T
    ) -> TreeNode[T]:
        if node is None:
            return TreeNode[T](value=value)
        if value > node.value:
            node.right = self._insert_recursive(
                node=node.right, 
                value=value,
            )
        else:
            node.left = self._insert_recursive(
                node=node.left, 
                value=value,
            )
        return node
    
    def erase(self, *, value: T) -> None:
        self._root, deleted = self._erase_recursive(
            node=self._root,
            value=value,
        )
        if deleted:
            self._size -= 1
    
    def _erase_recursive(
        self, 
        *, 
        node: TreeNode[T] | None, 
        value: T
    ) -> tuple[TreeNode[T] | None, bool]:
        if node is None:
            return None, False 
        if value > node.value:
            new_node, deleted = self._erase_recursive(
                node=node.right,
                value=value,
            )
            node.right = new_node
            return node, deleted
        elif value < node.value:
            new_node, deleted = self._erase_recursive(
                node=node.left,
                value=value,
            )
            node.left = new_node
            return node, deleted
        else:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            
            min_node = node.right
            while min_node.left is not None:
                min_node = min_node.left
            
            node.value = min_node.value
            new_node, deleted = self._erase_recursive(
                node=node.right,
                value=min_node.value,
            )
            node.right = new_node
            return node, deleted
    
    def find(self, *, value: T) -> bool:
        iterator = self._root
        while iterator is not None:
            if value > iterator.value:
                iterator = iterator.right
            elif value < iterator.value:
                iterator = iterator.left
            else:
                return True
        return False
    
    def size(self) -> int:
        return self._size
                
#################################################################

def test_insert() -> None:
    tree = BinarySearchTree[int]()

    tree.insert(value=10)
    tree.insert(value=5)
    tree.insert(value=15)

    assert tree.size() == 3
    assert tree.find(value=10) is True
    assert tree.find(value=5) is True
    assert tree.find(value=15) is True


def test_find_not_existing() -> None:
    tree = BinarySearchTree[int]()

    tree.insert(value=1)
    tree.insert(value=2)

    assert tree.find(value=3) is False


def test_erase_leaf() -> None:
    tree = BinarySearchTree[int]()

    tree.insert(value=10)
    tree.insert(value=5)
    tree.insert(value=15)

    tree.erase(value=5)

    assert tree.size() == 2
    assert tree.find(value=5) is False
    assert tree.find(value=10) is True
    assert tree.find(value=15) is True


def test_erase_root() -> None:
    tree = BinarySearchTree[int]()

    tree.insert(value=10)
    tree.insert(value=5)
    tree.insert(value=15)

    tree.erase(value=10)

    assert tree.size() == 2
    assert tree.find(value=10) is False
    assert tree.find(value=5) is True
    assert tree.find(value=15) is True


def test_erase_not_existing() -> None:
    tree = BinarySearchTree[int]()

    tree.insert(value=10)

    tree.erase(value=999)

    assert tree.size() == 1
    assert tree.find(value=10) is True


def run_tests() -> None:
    test_insert()
    test_find_not_existing()
    test_erase_leaf()
    test_erase_root()
    test_erase_not_existing()

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()