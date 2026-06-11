# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        if not curr.next:
            return None
        while curr:
            size +=1
            curr = curr.next
        print(size)
        index = size -n # to be deleted
        if index == 0: # first node to be deleted
            return head.next
        if index == size:
            # last node to be deleted
            curr = head
            while curr.next.next:
                curr = curr.next
            curr.next.next = None

            


        print(index)
        curr_index = 0
        curr = head
        while curr_index != index-1:
            curr = curr.next
            curr_index +=1
        curr.next = curr.next.next
        return head
