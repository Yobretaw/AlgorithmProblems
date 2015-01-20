#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
using namespace std;

/* Given an array with n objects colored red, white or blue, sort them so that objects of
 * the same color are adjacent, with the colors in the ordered red, white and blue.
 * 
 * Here we use the integers 0, 1 and 2 to represent red, white and blue respectively.
 * 
 * Note: You are not supposed to use the library's sort function for this problem.
 * 
 * Follow up:
 *
 * A rather stright forward solution is a two-pass algorithm using counting sort.
 * (iterate the array counting number of 0's, 1's and 2's, then overwrite array with total
 * number of 0's, then 1's and followed by 2's).
 * 
 * Could you come up with an one-pass algorithm using only constant space?
 */
void sortColors1(vector<int>& a) {
  int n = a.size();
  int counts[3] = {0};

  for (int i = 0; i < n; ++i) {
    counts[a[i]]++;
  }
  for (int i = 0, index = 0; i < 3; ++i) {
    for (int j = 0; j < counts[i]; ++j) {
      a[index++] = i;
    }
  }
}

void sortColors2(vector<int>& a) {
  int n = a.size();
  int red = 0, blue = n - 1, i = 0;

  while(i <= blue) {
    if(a[i] == 0) swap(a[i++], a[red++]);
    else if(a[i] == 2) swap(a[i], a[blue--]);
    else i++;
  }
}

int main() {
  vector<int> a;
  for (int i = 0; i < 20; ++i) {
    a.push_back(i % 3);
  }
  sortColors2(a);
  for (int i = 0; i < a.size(); ++i) {
    cout << a[i] << " ";
  }
  return 0;
}
