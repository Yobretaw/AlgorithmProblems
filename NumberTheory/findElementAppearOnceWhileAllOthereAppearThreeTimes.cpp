#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

int findOneInTwo(const vector<int>& arr) {
  int ret = 0;
  int len = arr.size();

  for(int i = 0; i < len; ++i) {
    ret ^= arr[i];
  }

  return ret;
}

int findOneInThree(const vector<int>& arr) {
  int ones = 0, twos = 0;
  int common_bit_mask;

  for (int i = 0; i < arr.size(); i++) {
    /**
     * The expression 'ones & arr[i]' gives the bits that are
     * there in both 'ones' and new element from arr[]. We add
     * these bits to 'twos' using bitwise OR
     */
    twos |= ones & arr[i];

    /**
     * XOR the new bits with previous 'ones' to get all bits
     * appearing odd number of times
     */
    ones ^= arr[i];

    /**
     * The common_bit_mask are those bits which appears third
     * times so they shouldn't appear in both 'ones' and 'twos'
     * common_bit_mask contains all these bits as 0, so that
     * these bits can be removed from 'ones' and 'twos'
     */
    common_bit_mask = ~(ones & twos);

    /**
     * Remove those bits that have appeared three times from
     * 'ones' and 'twos'
     */
    ones &= common_bit_mask;
    twos &= common_bit_mask;
  }

  return ones;
}

int main() {
  //vector<int> arr = {3, 3, 2, 3, 2, 2, 1, 1, 4, 1};
  //cout << findOneInThree(arr) << endl;
  
  vector<int> arr = {1, 2, 3, 2, 3, 1, 4, 5, 5};
  cout << findOneInTwo(arr) << endl;
  return 0;
}
