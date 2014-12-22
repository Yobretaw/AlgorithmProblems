#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
using namespace std;


int getNextDigit(vector<int>& digits, int m);

/* The set [1, 2, 3, ... n] contains a total of n! unique
 * permutations. By listign all of them in order, when n = 3
 * we have
 *  
 * 1, 2, 3
 * 1, 3, 2
 * 2, 1, 3
 * 2, 3, 1
 * 3, 1, 2
 * 3, 2, 1
 * 
 * Now given 0 <= n <= 9 and k, return the kth permutation sequence.
 */
vector<int> findSeq(int n, int k) {
  vector<int> fac(n);

  // generate factorials from 0 to n - 1
  for(int i = 0; i < n; i++) {
    fac[i] = i == 0 ? 1 : fac[i - 1] * i;
  }

  vector<int> digits(n, 0);
  vector<int> result(n, 0);
  k--;

  // reverse Canto expansion
  for(int i = 0; i < n; ++i) {
    int currFac = k / fac[n - 1 - i];
    int idx     = getNextDigit(digits, currFac);

    // ith digit of the result sequence is found
    result[i]   = idx;

    k %= fac[n - 1 - i];
  }
  return result;
}


// find i such that i is available and there are exactly
// m digits smaller than i are available
//
// i is available iff digits[i] = 0
int getNextDigit(vector<int>& digits, int m) {
  int i;
  for(i = 0; i < digits.size(); ++i) {
    if(!digits[i]) {
      if(m == 0) break;
      m--;
    }
  }
  digits[i] = 1;
  return i;
}

int main() {
  vector<int> res = findSeq(10, 5);
  for (int i = 0; i < res.size(); i++) {
    cout << res[i];
  }
  cout << endl;
  return 0;
}
