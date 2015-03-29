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

/* 问题定义：对于给定序列a1,a2,a3……an,寻找它的某个连续子段，
 * 使得其和最大。如( -2,11,-4,13,-5,-2 )最大子段是{ 11,-4,13 }其和为20。
 */


/*
 * 1. 枚举法
 * 
 * 以a[0]开始，求a[0], a[0] + a[1], a[0] + a[1] + a[2], ... a[0] + a[1] + ... + a[n - 1]
 * 以a[1]开始，求a[1], a[1] + a[2], a[1] + a[2] + a[3], ... a[1] + a[2] + ... + a[n - 1]
 * ...
 *
 * 以a[n - 1]开始， 求a[n - 1]
 * 一共n*(n-1)/2个连续字段，算法如下
 * 
 * time: O(n^2), space: O(1)
 */
int maxSubrange(const vector<int>& num, int& bestStart, int& bestEnd) {
  int n = num.size();
  int maxsum = 0;

  for (int start = 0; start < num.size(); ++start) {
    int sumStartHere = 0;
    for (int end = start; end < num.size(); ++end) {
      sumStartHere += num[end];
      if(sumStartHere > maxsum) {
        maxsum = sumStartHere;
        bestStart = start;
        bestEnd = end;
      }
    }
  }
  return maxsum;
}

/*
 * 1. 分冶法
 * 
 * time: O(nlogn), space: O(1)
 */
int maxSubrange2Help(const vector<int>& num, int begin, int end, int& bestStart, int& bestEnd) {
  if(begin == end) {
    bestStart = begin;
    bestEnd = begin;
    return num[begin] >= 0 ? num[begin] : 0;
  }

  int mid = begin + (end - begin) / 2;
  int leftbegin, leftend, rightbegin, rightend;
  int leftMax = maxSubrange2Help(num, begin, mid, leftbegin, leftend);
  int rightMax = maxSubrange2Help(num, mid + 1, end, rightbegin, rightend);


  int leftval = 0, leftmax = 0;
  int rightval = 0, rightmax = 0;
  int localStart = mid, localEnd = mid + 1;

  // extend to left
  for (int i = mid; i >= begin; --i) {
    leftval += num[i];
    if(leftval > leftmax) {
      leftmax = leftval;
      localStart = i;
    }
  }

  // extend to right 
  for (int i = mid + 1; i <= end; ++i) {
    rightval += num[i];
    if(rightval > rightmax) {
      rightmax = rightval;
      localEnd = i;
    }
  }
  
  // aggregate both left, right and cross part
  int sum = leftmax + rightmax;
  bestStart = localStart;
  bestEnd = localEnd;
  if(sum < leftMax) {
    sum = leftMax;
    bestStart = leftbegin;
    bestEnd = leftend;
  }
  if(sum < rightMax) {
    sum = rightMax;
    bestStart = rightbegin;
    bestEnd = rightend;
  }
  return sum;
}

int maxSubrange2(const vector<int>& num, int& bestStart, int& bestEnd) {
  return maxSubrange2Help(num, 0, num.size() - 1, bestStart, bestEnd);
}

/*
 *  3、最大m子段和问题
 *     (1)问题描述：给定由n个整数(可能为负数)组成的序列a1,a2,a3……an,以及一个正整数m,
 *     要求确定此序列的m个不相交子段的总和达到最大。最大子段和问题是最大m字段和问题当m=1时的特殊情形。
 *
 *     (2)问题分析：设b(i,j)表示数组a的前j项中i个子段和的最大值，且第i个子段含a[j](1<=i<=m,i<=j<=n),
 *     则所求的最优值显然为 max_{m <= j <= }(m, j)。与最大子段问题相似，计算b(i,j)的递归式为：
 *     
 *              b(i, j) = max{b(i, j - 1) + a[i], max_{i - 1 <= t <= j}(b(i - 1, t)) + a[j]}
 *
 *     其中，b(i, j - 1) + a[i] 表示第i个子段含a[j-1],而max_{i - 1 <= t <= j}(b(i - 1, t)) + a[j]项表示第i个子段仅含a[j]。
 *     初始时，b(0,j)=0,(1<=j<=n); b(i,0)=0,(1<=i<=m)。
 *     
 *
 *  给定n个数求这n个数划分成互不相交的m段的最大m子段和。
 *  
 *　经典的动态规划优化的问题。设f(i, j)表示前i个数划分成j段，且包括第i个数的最大m子段和，那么有状态转移方程：
 *　　　f(i, j) = max { f(i - 1, j) + v[i], max {f(k, j - 1) + v[i]}(k = j - 1 ... i - 1) }
 *　也就是说第i个数要么自己划到第j段，要么和前一个数一起划到第j段里面，转移是O(n)的，总复杂度O(mn^2)。
 *　可以引入一个辅助数组来优化转移。设g(i, j)表示前i个数划分成j段的最大子段和（注意第i个数未必在j段里面），那么递推关系如下：
 *　　　g(i, j) = max{g(i - 1, j), f(i, j)}，分是否加入第i个数来转移
 *　这样f的递推关系就变成：
 *　　　f(i, j) = max{f(i - 1, j), g(i - 1, j - 1)} + v[i]，转移变成了O(1)
 *　这样最后的结果就是g[n][m]，通过引入辅助数组巧妙的优化了转移。实现的时候可以用一维数组，速度很快。
 *     
 */
int maxSum(const vector<int>& a, int m) {
  int i, j, t;
  vector<int> f(a.size(), 0);     // f(i, j) = max { f(i - 1, j) + v[i], g(i - 1, j - 1) + v[i]}
  vector<int> g(a.size(), 0);     // g(i, j) = max{ g(i - 1, j), f(i, j) }

  for (i = 1; i <= a.size(); ++i) {
    t = min(i, m);
    for(j = 1; j <= t; j++) {
      f[j] = max(f[j], g[j - 1]) + a[i];
      g[j - 1] = max(g[j - 1], f[j - 1]);
    }
    g[j - 1] = max(g[j - 1], f[j - 1]);
  }
  return g[m];
}

int main() {
  //vector<int> num = {2, -1, 3};
  vector<int> num = { -2, 11, -4, 13, -5, -2 };
  //int left = 0;
  //int right = 0;
  //int maxval = maxSubrange2(num, left, right);
  //cout << left << " " << right << " " << maxval << endl;
  cout << maxSum(num, 2) << endl;
  return 0;
}
