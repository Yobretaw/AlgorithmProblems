#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

/* find the kth smallest element from two
 * sorted array
 *
 * time: O(logm + logn)
 */
int ksmall(int A[], int m, int B[], int n, int k) {
  if(k == m + n)
    return max(A[m-1], B[n-1]);

  // maintain invariant: i + j = k - 1
  int i = (int)((double)m / (m + n) * (k - 1));
  int j = k - 1 - i;

  int ai_1 = i == 0 ? INT_MIN : A[i - 1];
  int bj_1 = j == 0 ? INT_MIN : B[j - 1];
  int ai = i == m ? INT_MAX : A[i];
  int bj = i == n ? INT_MAX : B[j];

  if(bj_1 < ai && ai < bj)
    return ai;
  else if(ai_1 < bj && bj < ai)
    return bj;

  if(ai < bj)
    return ksmall(A+i+1, m-i-1, B, j, k-i-1);
  else
    return ksmall(A, i, B+j+1, n-j-1, k-j-1);
}


// http://fisherlei.blogspot.com/2012/12/leetcode-median-of-two-sorted-arrays.html
int getKSmall(int A[], int m, int B[], int n, int k) {
  if(m <= 0 || n <= 0) {
    return m == 0 ? B[k - 1] : A[k - 1];
  }
  
  if(k <= (m + n)/2) {
    if(A[m/2] < B[n/2])
      return getKSmall(A, m, B, n/2, k);
    else
      return getKSmall(A, m/2, B, n, k);
  } else {
    if(A[m/2] < B[n/2])
      return getKSmall(A, m/2, B, n, k - m/2 - 1);
    else
      return getKSmall(A, m, B + n/2, n, k - n/2 - 1);
  }
} 

double findMedianSortedArrays(int A[], int m, int B[], int n) {
  if((m + n) % 2 == 0)
    return (getKSmall(A, m, B, n, (m + n)/2) + getKSmall(A, m, B, n, (m + n)/2 + 1)) / 2.0;
  else
    return getKSmall(A, m, B, n, (m + n)/2 + 1);
}

int main() {
  int A[100];
  int B[100];
  for(int i = 0; i < 100; ++i) {
    A[i] = i + 1;
    B[i] = 100 + i + 1;
  }
  cout << findMedianSortedArrays(A, 100, B, 100) << endl;
  //for(int i = 0; i < 200; ++i) {
  //  cout << ksmall(A, 100, B, 100, i + 1) << endl;
  //}
  return 0;
}
