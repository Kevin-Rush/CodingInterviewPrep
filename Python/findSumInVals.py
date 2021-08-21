'''
2. Determine if the sum of two integers is equal to the given value
Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. Return true if the sum exists and return false if it does not. Consider this array and the target sums:

5
7
1
2
8
4
3
Target Sum
10
7+3=10, 2+8=10
Target Sum
19
No 2 values sum up to 19
'''

def find_sum_of_two(A, val):
    foundVals = set()
    for i in A:
        if val-i in foundVals:
            return True
        foundVals.add(i)
    return False


if __name__ == "__main__":
    for i in range(0, 10):
        print(i)
        print(find_sum_of_two([3, 7, 1, 2, 8, 4, 5], i))