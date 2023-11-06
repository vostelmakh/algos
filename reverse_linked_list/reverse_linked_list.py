from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self, head: Optional[ListNode]):
        while head != None:
            print("____")
            print("|", head.val, "|")
            print("____")
            print("|")

            head = head.next
        print("Nil")
        print("")

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head

        elements_count = 0

        while current:
            elements_count += 1
            current = current.next

        if (elements_count % 2 == 1):
            return False

        middle_element = int(elements_count//2)

        i = 0
    
        current = head

        while i < middle_element:
            current = current.next
            i += 1

        reversed_half_list = None

        while current:
            next_el = current.next

            current.next = reversed_half_list
            reversed_half_list = current

            current = next_el

        current = head
        rev_curent = reversed_half_list

        i = 0

        while i < middle_element:
            if rev_curent.val != current.val:
                return False

            rev_curent = rev_curent.next
            current = current.next

            i += 1
        
        return True

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        current = head
        
        while current:
            next_el = current.next

            current.next = new_list
            new_list = current

            current = next_el

        return new_list
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # append the remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next

n3 = ListNode(4, None)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

k3 = ListNode(4, None)
k2 = ListNode(3, k3)
k1 = ListNode(1, k2)

sol = Solution()

sol.mergeTwoLists(n1, k1)