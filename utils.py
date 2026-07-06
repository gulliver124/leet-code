class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def print_linked_list(node):
    """Print a linked list in a readable arrow-separated format."""
    values = linked_list_to_list(node)
    print(" -> ".join(str(v) for v in values) if values else "Empty list")