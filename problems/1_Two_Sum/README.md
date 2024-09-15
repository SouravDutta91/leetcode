# 1. Two Sum

## Problem statement

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


```
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
```
 

Constraints:
```
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
```
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

## Test case outputs

```
[0, 1]
[1, 2]
[0, 1]
```

## Notes

* `seen`: This dictionary or hash map stores the numbers that we have encountered so far along with their corresponding indices as values. 
* Iterate through the list: For each number, calculate its complement (i.e., `target - num`) and check if that complement is already in the dictionary or not. If it is, return the indices.
* If the complement is not found, we add the current number to the dictionary `seen`.

## Time Complexity

Our solution meets the time complexity requirement of less than $O(n^2)$.

* We iterate through the input number list exactly once. This results in a time complexity of $O(n)$, where $n$ is the number of elements in the list `nums`.
* Dictionary / Hash Map operations: 
    * Look up the complement in the hashmap: This takes $O(1)$ on average.
    * Insert the current number in the hashmap: This also takes $O(1)$ on average.

## Space Complexity

The space complexity here is also $O(n)$ because we store upto $n$ elements in the hash map.

I hope this solution and explanation is helpful to you. Happy coding, happy learning. :)