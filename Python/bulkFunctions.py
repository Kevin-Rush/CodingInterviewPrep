'''
9. How many ways can you make change with coins and a total amount
Suppose we have coin denominations of [1, 2, 5] and the total amount is 7. We can make 
changes in the following 6 ways:

Runtime Complexity: Quadratic, O(m*n)O(m∗n)

Memory Complexity: Linear, O(n)O(n)

To solve this problem, we’ll keep an array of size amount + 1. One additional space is reserved because we 
also want to store the solution for the 0 amount.

There is only one way you can make a change of 0, i.e., select no coin so we’ll initialize solution[0] = 1. 
We’ll solve the problem for each amount, denomination to amount, using coins up to a denomination, den.

The results of different denominations should be stored in the array solution. The solution for amount x using
a denomination den will then be:

solution[x] = solution[x] + solution[x - den]
We’ll repeat this process for all the denominations, and at the last element of the solution array, we will have 
the solution.
'''

def solve_coin_change(denominations, amount):
  solution = [0] * (amount + 1)
  solution[0] = 1;
  for den in denominations:
    for i in range(den, amount + 1):
      solution[i] += solution[i - den] 

  return solution[len(solution) - 1]

'''
10. Find Kth permutation
Given a set of ‘n’ elements, find their Kth permutation. Consider the following set of elements:

1
2
3
All permutations of the above elements are (with ordering):



Here we need to find the Kth permutation.


Runtime Complexity: Linear, O(n)O(n)

Memory Complexity: Linear, O(n)O(n)

Here is the algorithm that we will follow:

If input vector is empty return result vector
 
block_size = (n-1)! ['n' is the size of vector]

Figure out which block k will lie in and select the first element of that block
(this can be done by doing (k-1)/block_size)
 
Append selected element to result vector and remove it from original input vector
 
Deduce from k the blocks that are skipped i.e k = k - selected*block_size and goto step 1
'''

def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial(n -1 )

def find_kth_permutation(v, k, result):
  if not v:
    return
  
  n = len(v)
  # count is number of permutations starting with first digit
  count = factorial(n - 1)
  selected = (k - 1) // count
  
  result += str(v[selected])
  del v[selected]
  k = k - (count * selected)
  find_kth_permutation(v, k, result)

'''
11. Find all subsets of a given set of integers
We are given a set of integers and we have to find all the possible subsets of this set of 
integers. The following example elaborates on this further.

Given set of integers:

2
3
4
All possile subsets for the given set of integers:

2
3
2, 3
4
2, 4
3, 4
2, 3, 4

Runtime Complexity: Exponential, O(2^n*n)O(2
​n
​​ ∗n)

Memory Complexity: Exponential, O(2^n*n)O(2
​n
​​ ∗n)

There are several ways to solve this problem. We will discuss the one that is neat and 
easier to understand. We know that for a set of n elements there are 2^n2
​n
​​  subsets. For example, a set with 3 elements will have 8 subsets. Here is the algorithm we will use:

n = size of given integer set
subsets_count = 2^n
for i = 0 to subsets_count
    form a subset using the value of 'i' as following:
        bits in number 'i' represent index of elements to choose from original set,
        if a specific bit is 1 choose that number from original set and add it to current subset,
        e.g. if i = 6 i.e 110 in binary means that 1st and 2nd elements in original array need to be picked.
    add current subset to list of all subsets

'''

def get_bit(num, bit):
    temp = (1 << bit)
    temp = temp & num
    if temp == 0:
      return 0
    return 1
        
def get_all_subsets(v, sets):
    subsets_count = 2 ** len(v)
    for i in range(0, subsets_count):
      st = set([])
      for j in range(0, len(v)):
         if get_bit(i, j) == 1:
            st.add(v[j])
      sets.append(st)

'''
12. Print balanced brace combinations
Print all braces combinations for a given value n so that they are balanced. For this solution, 
we will be using recursion.

Runtime Complexity: Exponential, 2^n2
​n
​​ 

Memory Complexity: Linear, O(n)O(n)

The solution is to maintain counts of left_braces and right_braces. The basic algorithm is as follows:​

left_braces count: 0
right_braces count: 0
 
if left_braces count is less than n:
  add left_braces and recurse further
if right_braces count is less than left_braces count:
  add right_braces and recurse further
stop recursing when left_braces and right_braces counts are both equal to n
'''

import copy 

def print_all_braces_rec(n, left_count, right_count, output, result):

  if left_count >= n and right_count >= n:
    result.append(copy.copy(output));
    
  if left_count < n:
    output += '{'
    print_all_braces_rec(n, left_count + 1, right_count, output, result)
    output.pop()

  if right_count < left_count:
    output += '}'
    print_all_braces_rec(n, left_count, right_count + 1, output, result)
    output.pop()

def print_all_braces(n):
  output = []
  result = []
  print_all_braces_rec(n, 0, 0, output, result)
  return result

'''
13. Clone a Directed Graph
Given the root node of a directed graph, clone this graph by creating its deep 
copy so that the cloned graph has the same vertices and edges as the original graph.

Let’s look at the below graphs as an example. If the input graph is G = (V, E)G=(V,E) 
where V is set of vertices and E is set of edges, then the output graph (cloned graph) G’ = (V’, E’) 
such that V = V’ and E = E’. We are assuming that all vertices are reachable from the root vertex, 
i.e. we have a connected graph.

Runtime Complexity: Linear, O(n)O(n)

Memory Complexity: Logarithmic, O(logn)O(logn)

We use depth-first traversal and create a copy of each node while traversing the graph. To avoid 
getting stuck in cycles, we’ll use a hashtable to store each completed node and will not revisit 
nodes that exist in the hashtable. The hashtable key will be a node in the original graph, and its 
value will be the corresponding node in the cloned graph.

'''

class Node:
  def __init__(self, d):
    self.data = d
    self.neighbors = []

def clone_rec(root, nodes_completed):
  if root == None:
    return None

  pNew = Node(root.data)
  nodes_completed[root] = pNew

  for p in root.neighbors:
    x = nodes_completed.get(p)
    if x == None:
      pNew.neighbors += [clone_rec(p, nodes_completed)]
    else:
      pNew.neighbors += [x]
  return pNew

def clone(root):
  nodes_completed = {}
  return clone_rec(root, nodes_completed)

'''
14. Find Low/High Index
Given a sorted array of integers, return the low and high index of the given key. You must return -1 if the indexes are not found. The array length can be in the millions with many duplicates.

In the following example, according to the key, the low and high indices would be:

key: 1, low = 0 and high = 0
key: 2, low = 1 and high = 1
key: 5, low = 2 and high = 9
key: 20, low = 10 and high = 10


For the testing of your code, the input array will be:

1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6

Runtime Complexity: Logarithmic, O(logn)O(logn)

Memory Complexity: Constant, O(1)O(1)

Linearly scanning the sorted array for low and high indices are highly inefficient since our array size can be in millions. Instead, we will use a slightly modified binary search to find the low and high indices of a given key. We need to do binary search twice: once for finding the low index, once for finding the high index.

Let’s look at the algorithm for finding the low index. At every step, consider the array between low and high indices and calculate the mid index.

If the element at mid index is less than the key, low becomes mid + 1 (to move towards the start of range).
If the element at mid is greater or equal to the key, the high becomes mid - 1. Index at low remains the same.
When low is greater than high, low would be pointing to the first occurrence of the key.
If the element at low does not match the key, return -1.
Similarly, we can find the high index by slightly modifying the above condition:

Switch the low index to mid + 1 when element at mid index is less than or equal to the key.
Switch the high index to mid - 1 when the element at mid is greater than the key.

'''

def find_low_index(arr, key):
  
  low = 0
  high = len(arr) - 1
  mid = int(high / 2)

  while low <= high:

    mid_elem = arr[mid]

    if mid_elem < key:
      low = mid + 1
    else:
      high = mid - 1

    mid = low + int((high - low) / 2)

  if low < len(arr) and arr[low] == key:
    return low

  return -1

def find_high_index(arr, key):
  low = 0
  high = len(arr) - 1
  mid = int(high / 2)

  while low <= high:
    mid_elem = arr[mid]

    if mid_elem <= key:
      low = mid + 1
    else:
      high = mid - 1

    mid = low + int((high - low) / 2);
  
  if high == -1:
    return high

  if high < len(arr) and arr[high] == key:
    return high

  return -1

'''
15. Search Rotated Array
Search for a given number in a sorted array, with unique elements, that has been rotated by 
some arbitrary number. Return -1 if the number does not exist. Assume that the array does not contain duplicates.

Runtime Complexity: Logarithmic, O(logn)O(logn)

Memory Complexity: Logarithmic, O(logn)O(logn)

The solution is essentially a binary search but with some modifications. If we look at the array in the 
example closely, we notice that at least one half of the array is always sorted. We can use this property 
to our advantage. If the number n lies within the sorted half of the array, then our problem is a basic 
binary search. Otherwise, discard the sorted half and keep examining the unsorted half. Since we are 
partitioning the array in half at each step, this gives us O(log n)O(logn) runtime complexity.
'''
def binary_search_rotated(arr, key):
  start = 0
  end = len(arr) - 1

  if start > end:
    return -1
    
  while start <= end:
    mid = start + (end - start) // 2

    if arr[mid] == key:
      return mid

    if arr[start] <= arr[mid] and key <= arr[mid] and key >= arr[start]:
      end = mid - 1
    
    elif (arr[mid] <= arr[end] and key >= arr[mid] and key <= arr[end]):
      start = mid + 1

    elif arr[start] <= arr[mid] and arr[mid] <= arr[end] and key > arr[end]:
      start = mid + 1 

    elif arr[end] <= arr[mid]:
      start = mid + 1  

    elif arr[start] >= arr[mid]:
      end = mid - 1
    
    else:
      return -1
    
  return -1

'''
More common Amazon coding interview questions
K largest elements from an array
Convert a Binary tree to DLL
Given a binary tree T, find the maximum path sum. The path may start and end at any node in the tree.
Rotate a matrix by 90 degrees
Assembly line scheduling with dynamic programming
Implement a stack with push(), min(), and pop() in O(1)O(1) time
How do you rotate an array by K?
Design Snake Game using Object Oriented analysis and design technique.
Print all permutations of a given string using recursion
Implement a queue using a linked list
Find the longest increasing subsequence of an array
Lowest common ancestor in a Binary Search Tree and Binary Tree
Rotate a given list to the right by k places, which is non-negative.
Write a function that counts the total of set bits in a 32-bit integer.
How do you detect a loop in a singly linked list?
Reverse an array in groups
Given a binary tree, check if it’s a mirror of itself
Josephus problem for recursion
Zero Sum Subarrays
Huffman Decoding for greedy algorithms
Egg Dropping Puzzle for dynamic programming
N-Queen Problem
Check if strings are rotations of each other
0-1 Knapsack Problem
Unbounded knapsack problem
Longest palindromic subsequence
Print nth number in the Fibonacci series
Longest common substring
Longest common subsequence
'''
