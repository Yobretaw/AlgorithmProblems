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
 * Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
 * 
 * The same repeated number may be chosen from C unlimited number of times.
 * 
 * Note:
 * All numbers (including target) will be positive integers.
 * Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
 * The solution set must not contain duplicate combinations.
 * For example, given candidate set 2,3,6,7 and target 7, the solution set is: 
 *     [7] 
 *     [2, 2, 3] 
 */

void sumHelp(const vector<int>& numbers, int idx, int target, vector<int>& path, vector<vector<int> >& result) {
  if(idx == numbers.size() || target <= 0) {
    if(target == 0) {
      result.push_back(path);
    }
    return;
  }

  path.push_back(numbers[idx]);
  sumHelp(numbers, idx, target - numbers[idx], path, result);
  path.pop_back();
  sumHelp(numbers, idx + 1, target, path, result);
}

vector<vector<int> > sum(vector<int>& numbers, int target) {
  vector<vector<int> > result;
  vector<int> path;
  sort(numbers.begin(), numbers.end());
  sumHelp(numbers, 0, target, path, result);
  return result;
}

/*
 * Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
 * 
 * Each number in C may only be used once in the combination.
 * 
 * Note:
 * All numbers (including target) will be positive integers.
 * Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
 * The solution set must not contain duplicate combinations.
 * For example, given candidate set 10,1,2,7,6,1,5 and target 8, a solution set is: 
 *    [1, 7] 
 *    [1, 2, 5] 
 *    [2, 6] 
 *    [1, 1, 6] 
 */
void sumHelp2(const vector<int>& numbers, int idx, int target, vector<int>& path, vector<vector<int> >& result) {
  if(idx == numbers.size() || target <= 0) {
    if(target == 0)
      result.push_back(path);
    return;
  }


  int i = idx;
  int count = 0;
  while(i < numbers.size() && numbers[i] == numbers[idx]) {
    count++;
    i++;
  }

  sumHelp2(numbers, idx + count, target, path, result);

  for (int i = 1; i <= count; ++i) {
    path.push_back(numbers[idx]);
    sumHelp2(numbers, idx + count, target - numbers[idx] * i, path, result);
  }
  
  for(int i = 0; i < count; ++i)
    path.pop_back();
}

vector<vector<int> > sumWithBound(vector<int>& numbers, int target) {
  vector<vector<int> > result;
  vector<int> path;
  sort(numbers.begin(), numbers.end());
  sumHelp2(numbers, 0, target, path, result);
  return result;
}

int main() {
  vector<int> numbers = {10, 1, 2, 7, 6, 1, 5};
  vector<vector<int> > result = sumWithBound(numbers, 8);
  for (int i = 0; i < result.size(); ++i) {
    for (int j = 0; j < result[i].size(); ++j) {
      cout << result[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}
