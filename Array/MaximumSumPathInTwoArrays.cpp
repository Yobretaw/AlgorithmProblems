#include<iostream>
#include <vector>
using namespace std;

/*
Given two sorted arrays such the arrays may have some common elements. Find the sum of the maximum sum path to reach from beginning of any array to end of any of the two arrays. We can switch from one array to another array only at common elements.

Expected time complexity is O(m+n) where m is the number of elements in ar1[] and n is the number of elements in ar2[].

Examples:

Input:  ar1[] = {2, 3, 7, 10, 12}, ar2[] = {1, 5, 7, 8}
Output: 35
35 is sum of 1 + 5 + 7 + 10 + 12.
We start from first element of arr2 which is 1, then we
move to 5, then 7.  From 7, we switch to ar1 (7 is common)
and traverse 10 and 12.

Input:  ar1[] = {10, 12}, ar2 = {5, 7, 9}
Output: 22
22 is sum of 10 and 12.
Since there is no common element, we need to take all 
elements from the array with more sum.

Input:  ar1[] = {2, 3, 7, 10, 12, 15, 30, 34}
        ar2[] = {1, 5, 7, 8, 10, 15, 16, 19}
Output: 122
122 is sum of 1, 5, 7, 8, 10, 12, 15, 30, 34
*/


// This function returns the sum of elements on maximum path
// from beginning to end
int maxPathSum(const vector<int>& ar1, const vector<int>& ar2)
{
    // initialize indexes for ar1[] and ar2[]
    int i = 0, j = 0;
    int m = ar1.size(), n = ar2.size();
 
    // Initialize result and current sum through ar1[] and ar2[].
    int  result = 0, sum1 = 0, sum2 = 0;
 
    // Below 3 loops are similar to merge in merge sort
    while (i < m && j < n)
    {
        // Add elements of ar1[] to sum1
        if (ar1[i] < ar2[j])
            sum1 += ar1[i++];
 
        // Add elements of ar2[] to sum2
        else if (ar1[i] > ar2[j])
            sum2 += ar2[j++];
 
        else  // we reached a common point
        {
            // Take the maximum of two sums and add to result
            result += max(sum1, sum2);
 
            // Update sum1 and sum2 for elements after this
            // intersection point
            sum1 = 0, sum2 = 0;
 
            // Keep updating result while there are more common
            // elements
            while (i < m &&  j < n && ar1[i] == ar2[j])
            {
                result = result + ar1[i];
                i++;
                j++;
            }
        }
    }
 
    // Add remaining elements of ar1[]
    while (i < m)
        sum1  +=  ar1[i++];
 
    // Add remaining elements of ar2[]
    while (j < n)
        sum2 +=  ar2[j++];
 
    // Add maximum of two sums of remaining elements
    result +=  max(sum1, sum2);
 
    return result;
}
 
// Driver program to test above function
int main()
{
    vector<int> ar1 = {2, 3, 7, 10, 12, 15, 30, 34};
    vector<int> ar2 = {1, 5, 7, 8, 10, 15, 16, 19};
    cout << maxPathSum(ar1, ar2) << endl;
    return 0;
}
