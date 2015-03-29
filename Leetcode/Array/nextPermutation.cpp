#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <climits>
using namespace std;

/* Implement next permutation, which rearranges numbers
 * into the lexicographically next greater permutation 
 * of numbers.
 *
 * If such arrangement is not possible, it must rearranges
 * it as the lowest possible order(i.e sorted in ascending
 * order).
 *
 * The replacement must be in-place.
 *
 * Example:
 *
 *    1, 2, 3 -> 1, 3, 2
 *    3, 2, 1 -> 1, 2, 3
 *    1, 1, 5 -> 1, 5, 1
 *
 * */
void nextPermutation(vector<int>& num) {
  int len = num.size();

  if(len < 2)
    return;

  // find the last index i such that num[i] < num[i+1]
  int i;
  for(i = len - 1; i >= 1; --i) {
    if(num[i] > num[i - 1])
      break;
  }
  i--;

  if(i == -1) {
    // already in its maximum form
    for(int i = 0; i < len / 2; ++i) {
      swap(num[i], num[len - i - 1]);
    }
    return;
  }

  // find the smallest digit that is larger than num[i]
  // from (i + 1) to len
  int idx;
  int diff = INT_MAX;
  for(int j = len - 1; j > i; --j) {
    if(num[j] > num[i] && (diff > (num[j] - num[i]))) {
      idx = j;
      diff = num[j] - num[i];
    }
  }

  // swap num[i] and num[idx], and reverse all digits
  // in the range [i + 1, len)
  swap(num[i], num[idx]);
  while(i < len) {
    swap(num[++i], num[--len]);
  }
  return;
}

int main() {
  //vector<int> num = {1, 2, 3, 2, 6, 5, 3};
  //vector<int> num = {6, 8, 7, 4, 3, 2};
  vector<int> num = {7, 6, 5, 4, 3, 2, 1};
  for(int i = 0; i < num.size(); i++)
    cout << num[i];
  cout << endl;

  nextPermutation(num);

  for(int i = 0; i < num.size(); i++)
    cout << num[i];
  cout << endl;
  return 0;
}
