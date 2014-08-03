#include "iostream"
#include "assert.h"
#include "vector"
using namespace std;

int find(int a[], int m, int b[], int n, int k) {

  assert(m >= 0);
  assert(n >= 0);
  assert(k > 0);
  assert(k <= m+n);

  int i = (int)((double)m / (m + n) * (k - 1));
  int j = (k - 1) - i;

  assert(i >= 0);
  assert(j >= 0);
  assert(i <= m);
  assert(j <= n);

  int ai_1 = ((i == 0) ? INT_MIN : a[i - 1]);
  int bj_1 = ((j == 0) ? INT_MIN : b[j - 1]);
  int ai = ((i == m) ? INT_MAX : a[i]);
  int bj = ((j == n) ? INT_MAX : b[j]);

  if(bj_1 <= ai && ai <= bj)
    return ai;
  else if(ai_1 <= bj && bj <= ai)
    return bj;

  if(ai < bj)
    return find(a+i+1, m-i-1, b, j, k-i-1);
  else
    return find(a, i, b+j+1, n-j-1, k-j-1);
}


int main()
{
  int a[] = { 1, 2, 3, 4, 5 };
  int b[] = { 1, 2, 3, 4, 5 };
  //int b[] = { 6, 7, 8, 9, 10 };
  cout << find(a, 5, b, 5, 1) << endl;
  cout << find(a, 5, b, 5, 2) << endl;
  cout << find(a, 5, b, 5, 3) << endl;
  cout << find(a, 5, b, 5, 4) << endl;
  cout << find(a, 5, b, 5, 5) << endl;
  cout << find(a, 5, b, 5, 6) << endl;
  cout << find(a, 5, b, 5, 7) << endl;
  cout << find(a, 5, b, 5, 8) << endl;
  cout << find(a, 5, b, 5, 9) << endl;
  cout << find(a, 5, b, 5, 10) << endl;
  return 0;
}
