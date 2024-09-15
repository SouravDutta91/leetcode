# 2. Add Two Numbers

## Problem statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


```
Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

```
 

Constraints:

```
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
```
 
## Test case outputs

```
[7, 0, 8]
[0]
[8, 9, 9, 9, 0, 0, 0, 1]
```

## Notes

* `dummy`: The dummy node is used to simplify the construction of the result linked list. We return `dummy.next` at the end.
* `carry`: The carry is initially set to 0. At every step, we calculate the sum of the corresponding digits from `l1`, `l2`, and the `carry`. If the sum is 10 or more, then we update the carry for the next step.
* **Node values**: The last digit is extracted using `total % 10`. The carry is updated using `total // 10`.
* `create_linked_list()`: This function takes a list of integers and creates a linked list where each node represents a digit.
* `print_linked_list()`: This function takes a linked list and prints it as a list of integers.

## Time Complexity

$O(max(n, m))$

Let $n$ be the number of nodes in the first linked list `l1`.

Let $m$ be the number of nodes in the second linked list `l2`.

In the worst case, both linked lists will have to be traversed fully. Hence, the time complexity is $O(max(n, m))$.

## Space Complexity

$O(max(n, m))$

Let $n$ be the number of nodes in the first linked list `l1`.

Let $m$ be the number of nodes in the second linked list `l2`.

The space complexity here is determined by the size of the output linked list. In the worst case, it will have the same number of nodes as the longer of the two input lists, plus another node maybe of the carry element. Thus, the space complexity here is also $O(max(n, m))$, as `val1`, `val2`, and `carry` require constant space.

I hope this solution and explanation is helpful to you. Happy coding, happy learning. :)