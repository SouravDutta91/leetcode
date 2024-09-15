# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Initialise a dummy node and a current pointer
        dummy = ListNode()
        current = dummy
        carry = 0

        # Iterate through both the linked lists
        while l1 or l2 or carry:

            # Get values from the nodes, or 0 if the node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of the values and the carry
            total = val1 + val2 + carry

            # Update the carry
            carry = total // 10

            # Get the current digit
            new_val = total % 10

            # Create a new node with the sum and update the pointer
            current.next = ListNode(new_val)
            current = current.next

            # Move to the next node in the list if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the sum list, starting from the next node of the dummy
        return dummy.next


# Create a linked list from an input list of numbers
def create_linked_list(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


# Print the linked list as a list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)


# main function
def main():

    # Create an instance of the Solution class
    solution = Solution()
    
    # Test case 1: l1 = [2, 4, 3], l2 = [5, 6, 4]
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print_linked_list(result)  # Expected output: [7, 0, 8]

    # Test case 2: l1 = [0], l2 = [0]
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print_linked_list(result)  # Expected output: [0]

    # Test case 3: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    print_linked_list(result)  # Expected output: [8, 9, 9, 9, 0, 0, 0, 1]


# Run the main function
if __name__ == "__main__":
    main()