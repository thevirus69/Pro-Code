#include <stdio.h>
 
// Function to determine if target exists in a sorted array `A` or not
// using an interpolation search algorithm
int interpolationSearch(int A[], int n, int target)
{
    // base case
    if (n == 0) {
        return -1;
    }
 
    // search space is A[low…high]
    int low = 0, high = n - 1, mid;
 
    while (A[high] != A[low] && target >= A[low] && target <= A[high])
    {
        // estimate mid
        mid = low + ((target - A[low]) * (high - low) / (A[high] - A[low]));
 
        // target value is found
        if (target == A[mid]) {
            return mid;
        }
        // discard all elements in the right search space, including the middle element
        else if (target < A[mid]) {
            high = mid - 1;
        }
        // discard all elements in the left search space, including the middle element
        else {
            low = mid + 1;
        }
    }
 
    // if a target is found
    if (target == A[low]) {
        return low;
    }
 
    // target doesn't exist in the array
    else {
        return -1;
    }
}
 
int main(void)
{
    int A[] = {2, 5, 6, 8, 9, 10};
    int target = 5;
 
    int n = sizeof(A)/sizeof(A[0]);
    int index = interpolationSearch(A, n, target);
 
    if (index != -1) {
        printf("Element found at index %d", index);
    }
    else {
        printf("Element not found in the array");
    }
 
    return 0;
}
