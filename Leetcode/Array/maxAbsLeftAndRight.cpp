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

/*                                最大的LeftMax与rightMax之差绝对值
 *                                
 *  给定一个长度为N的整型数组arr，可以划分成左右两个部分： 左部分arr[0..K]，右部分arr[K+1..arr.length-1]，
 *  K可以取值的范围是[0,arr.length-2] 求这么多划分方案中，左部分中的最大值减去右部分最大值的绝对值，最大是多少？
 *  
 *  例如： [2,7,3,1,1] 当左部分为[2,7]，右部分为[3,1,1]时，左部分中的最大值减去右部分最大值的绝对值为4;
 *  当左部分为[2,7,3]，右部分为[1,1]时，左部分中的最大值减去右部分最大值的绝对值为6; 最后返回的结果为6。
 *  注意：如果数组的长度为N，请尽量做到时间复杂度O(N)，额外空间复杂度O(1)
 */
int getMaxAbsLeftAndRight(const vector<int>& num) {
  int len = num.size();
  
  int maxval = INT_MIN;
  for(auto val : num) maxval = max(maxval, val);

  return max(maxval - num[0], maxval - num[len - 1]);
}

int main() {
  return 0;
}
