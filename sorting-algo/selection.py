"""
Selection Sort is a simple sorting algorithm that works by repeatedly 
finding the minimum element from the unsorted part of the array and 
putting it at the beginning. The algorithm maintains two subarrays within the given array:
1. The subarray which is already sorted.
2. The remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element from the unsorted subarray 
is picked and moved to the sorted subarray. The time complexity of Selection Sort is 
O(n^2) in all cases (best, average, and worst), making it inefficient for large lists. 
However, it is easy to understand and implement.
"""