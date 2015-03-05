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
 * 给定一个长度为n的数列{a1,a2...an}，每次可以选择一个区间[l,r]，使这个区间内的数都加一或者都减一。
 * 问至少需要多少次操作才能使数列中的所有数都一样,并求出在保证最少次数的前提下,最终得到的数列有多少种。
 * 
 *
 * 考虑差分后的序列
 * 每次对[l,r]进行+1/-1，相当于在差分后的数组上对l进行+1/-1，然后对r+1进行-1/+1
 * 特殊的，如果r=n，那么就相当于对l进行了+1/-1
 * 我们最终的目标是将差分数组变成第一个位置是最终的数字，2~n都是0
 * 那么我们统计差分后的数组的2~n号位置上每个位置上的数
 * 令pos为所有正数的和，neg为所有负数的和的绝对值
 * 那么首先是pos和neg对消 可能会剩下
 * 剩下的有两种选择：自己消掉或者与1号位置对消
 * 故第一问答案为max(pos,neg) 第二问答案为abs(pos-neg)+1
 * 
 */
void calcOps(const vector<int>& arr, int& minOp, int& amount) {
  int n = arr.size();
  vector<int> diff(n, 0);

  for (int i = 1; i < n; ++i) {
    diff[i] = arr[i] - arr[i - 1];
  }

  int pos = 0, neg = 0;
  for (int i = 1; i < n; ++i) {
    if(diff[i] > 0) pos += diff[i];
    else neg += -diff[i];
  }

  minOp = max(pos, neg);
  amount = abs(pos - neg) + 1;
  return;
}

int main() {
  return 0;
}
