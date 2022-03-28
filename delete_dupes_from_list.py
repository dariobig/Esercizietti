# Definition for singly-linked list.

# %%
from __future__ import annotations
from typing import Optional, List, Iterable

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, values: List[int]) -> Optional[ListNode]:
        if not values:
            return None
        head = ListNode()
        node = head
        for v in values:
            node.val = v
            node.next = ListNode()
        return head

    def __eq__(self, other: Optional[ListNode]) -> bool:
        node = other
        current = self
        while node and node.next:
            if not current or current.val != node.val:
                return False
            current = current.next
            node = node.next
        return True

    def __print__(self) -> str:
        node = self
        values = []
        while node and node.next:
            node = node.next
            values.append(node.v)
            print(node.v)

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique = set()
        node = head.next
        prev = head
        while node and node.next:
            if node.val not in unique:
                unique.add(node.val)
                print(f'val: {node.val}')
                continue
            if node and node.next:
                print(f'val: {node.val}')
            node.next = node.next #advance
        print(unique)
        return head


print(ListNode.from_list([1,2,3,3,4,4,5]) == ListNode.from_list([1,2,3,3,4,4,5]))

Tests = [([1,2,3,3,4,4,5],[1,2,5]), ([1,1,1,2,3],[2,3]), (
[1,2,3,3,4,4,5], [1, 2, 3, 4, 5])]
s = Solution()
for original, deduped in Tests:
    res = print(s.deleteDuplicates(ListNode.from_list(original)))
    print(res == ListNode.from_list(deduped))
