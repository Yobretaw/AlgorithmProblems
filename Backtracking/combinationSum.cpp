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

int main() {
  vector<int> numbers = {1, 2};
  vector<vector<int> > result = sum(numbers, 3);
  for (int i = 0; i < result.size(); ++i) {
    for (int j = 0; j < result[i].size(); ++j) {
      cout << result[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}
