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

void dfs(const vector<int>& sorted, int idx, vector<int>& path, vector<vector<int> >& result);

vector<vector<int> > subset(const vector<int>& a) {
  vector<int> sorted(a);
  sort(sorted.begin(), sorted.end());

  vector<vector<int> > result;
  vector<int> path;

  dfs(sorted, 0, path, result);
  return result;
}

void dfs(const vector<int>& sorted, int idx, vector<int>& path, vector<vector<int> >& result) {
  // pass duplicates
  while(idx > 0 && idx < sorted.size() && sorted[idx] == sorted[idx - 1]) idx++;

  if(idx == sorted.size()) {
    result.push_back(path);
    return;
  }

  // does not include sorted[idx]
  dfs(sorted, idx + 1, path, result);

  // includ sorted[idx]
  path.push_back(sorted[idx]);
  dfs(sorted, idx + 1, path, result);

  path.pop_back();
}

vector<vector<int> >subsetIterative(const vector<int>& a) {
  vector<int> sorted(a);
  sort(sorted.begin(), sorted.end());

  int curr = 0;
  for (int i = 0; i < sorted.size(); ++i) {
    if(i > 0 && sorted[i] == sorted[i - 1]) continue;
    sorted[curr++] = sorted[i];
  }
  sorted.resize(curr);


  vector<int> v;
  vector<vector<int> > result(1 << n);

  int n = sorted.size(), count = 0;
  for (int i = 0; i < 1 << n; ++i) {
    for (int j = 0; j < n; ++j)
      if(i & 1 << j) v.push_back(sorted[j]);

    result[count++] = v;
    v.clear();
  }
  return result;
}


int main() {
  vector<int> a;
  for (int i = 0; i < 4; ++i) {
    a.push_back(i);
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
