from utils import ListNode, build_linked_list, linked_list_to_list

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return dummy_head.next

if __name__=="__main__":
    l1 = build_linked_list([2, 4, 3])   
    l2 = build_linked_list([5, 6, 4])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print(linked_list_to_list(result))