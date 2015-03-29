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

void subsetHelp(const vector<int>& a, vector<int>& path, int step, vector<vector<int> >& result);
void subsetHelpSizeK(const vector<int>& a, vector<int>& path, int step, vector<vector<int> >&result, int k);

vector<vector<int> > subset(const vector<int>& a) {
  vector<int> sorted(a);
  sort(sorted.begin(), sorted.end());

  vector<vector<int> > result;
  vector<int> path;

  //subsetHelp(sorted, path, 0, result);
  subsetHelpSizeK(sorted, path, 0, result, 6);
  return result;
}

void subsetHelp(const vector<int>& a, vector<int>& path, int step, vector<vector<int> >& result) {
  if(step == a.size()) {
    result.push_back(path);
    return;
  }
  // does not include a[step]
  subsetHelp(a, path, step + 1, result);

  // include a[step]
  path.push_back(a[step]);
  subsetHelp(a, path, step + 1, result);
  
  path.pop_back();
}

// return result for all subset with size equals to k
void subsetHelpSizeK(const vector<int>& a, vector<int>& path, int step, vector<vector<int> >&result, int k) {
  if(step == a.size()) return;

  // return if size reached k
  if(path.size() == k) {
    result.push_back(path);
    return;
  }

  // does not include a[setp]
  subsetHelpSizeK(a, path, step + 1, result, k);

  // includ a[step]
  path.push_back(a[step]);
  subsetHelpSizeK(a, path, step + 1, result, k);

  path.pop_back();
}

vector<vector<int> >subsetIterative(const vector<int>& a) {
  vector<int> sorted(a);
  sort(sorted.begin(), sorted.end());

  int n = sorted.size();
  int count = 0;
  vector<vector<int> > result(1 << n);
  vector<int> v;
  for (int i = 0; i < 1 << n; ++i) {
    for (int j = 0; j < n; ++j) {
      if(i & 1 << j) v.push_back(sorted[j]);
    }
    result[count++] = v;
    v.clear();
  }
  return result;
}

int main() {
  vector<int> a;
  for (int i = 0; i < 3; ++i) {
    a.push_back(i);
  }
  //vector<vector<int> > result = subset(a);
  vector<vector<int> > result = subsetIterative(a);
  for (int i = 0; i < result.size(); ++i) {
    for (int j = 0; j < result[i].size(); ++j) {
      cout << result[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}
