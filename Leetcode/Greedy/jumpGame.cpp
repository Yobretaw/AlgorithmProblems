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

/*
 * Given an array of non-negative integers, you are initially positioned at the first index of the array.
 * 
 * Each element in the array represents your maximum jump length at that position.
 * 
 * Determine if you are able to reach the last index.
 * 
 * For example:
 *   A = [2,3,1,1,4], return true.
 *   A = [3,2,1,0,4], return false.
 */
bool jump(const vector<int>& num) {
  int reach = 1;
  for (int i = 0; i < reach && reach < num.size(); ++i)
    reach = max(reach, i + 1 + num[i]);

  return reach >= num.size();
}

/*
 * Given an array of non-negative integers, you are initially positioned at the first index of the array.
 * 
 * Each element in the array represents your maximum jump length at that position.
 * 
 * Your goal is to reach the last index in the minimum number of jumps.
 * 
 * For example:
 *   Given array A = [2,3,1,1,4]
 * 
 * The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
 */
int minJump(vector<int>& num) {
  int result = 0;
  int last = 0;   // the max distance has been reached
  int curr = 0;   // the max distance can be reached using *result* steps

  for (int i = 0; i < num.size(); ++i) {
    if(i > last) {
      last = curr;
      ++result;
    }
    curr = max(curr, i + num[i]);
  }
  return result;
}

int main() {
  vector<int> num = {2, 3, 1, 1, 4};
  //vector<int> num = {3, 2, 1, 0, 4};
  //vector<int> num = {2, 0};
  //vector<int> num = {1,2,2,6,3,6,1,8,9,4,7,6,5,6,8,2,6,1,3,6,6,6,3,2,4,9,4,5,9,8,2,2,1,6,1,6,2,2,6,1,8,6,8,3,2,8,5,8,0,1,4,8,7,9,0,3,9,4,8,0,2,2,5,5,8,6,3,1,0,2,4,9,8,4,4,2,3,2,2,5,5,9,3,2,8,5,8,9,1,6,2,5,9,9,3,9,7,6,0,7,8,7,8,8,3,5,0};
  cout << minJump(num) << endl;
  return 0;
}
