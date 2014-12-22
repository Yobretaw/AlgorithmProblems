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

int main() {

  int A[1] = { 1 };
  int B[1] = { 2 };
  for(int i = 1; i <= 2; i++) {
    cout << "i: " << i << ", " << ksmall(A, 1, B, 1, i) << endl;
  }

  //int A[6] = { 0, 1, 2, 3, 4, 5 };
  //int B[6] = { 6, 7, 8, 9, 10, 11 };
  //for(int i = 1; i <= 12; i++) {
  //  cout << "i: " << i << ", " << ksmall(A, 6, B, 6, i) << endl;
  //}
  return 0;
}
