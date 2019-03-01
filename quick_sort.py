"""
Quick sort is also a divide and conquer algorithm like merge sort. 
Although it’s a bit more complicated, in most standard implementations it 
performs significantly faster than merge sort and rarely reaches its worst case 
complexity of O(n²). It has 3 main steps:

(1) We first select an element which we will call the pivot from the array.

(2) Move all elements that are smaller than the pivot to the left of the pivot; 
move all elements that are larger than the pivot to the right of the pivot. This 
is called the partition operation.

(3) Recursively apply the above 2 steps separately to each of the sub-arrays of 
elements with smaller and bigger values than the last pivot.
"""