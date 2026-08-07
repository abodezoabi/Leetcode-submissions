# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []

        # Store all values in arr
        for lst in lists:
            node = lst

            while node:
                arr.append(node.val)
                node = node.next

        # Sort values
        arr.sort()

        # Build linked list
        dummy = ListNode()
        tail = dummy

        for val in arr:
            tail.next = ListNode(val)
            tail = tail.next

        return dummy.next