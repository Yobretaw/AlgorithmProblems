#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

vector<int> findCommon(vector<int> a, vector<int> b) {
  if(a.empty() || b.empty()) {
    return vector<int>();
  }

  int ia = 0;
  int ib = 0;
  vector<int> result;

  sort(a.begin(), a.end());
  sort(b.begin(), b.end());
  
  while(ia < a.size() && ib < b.size()) {
    if(a[ia] == b[ib]) {
      result.push_back(a[ia]);
      ia++;
      ib++;
    } else if(a[ia] < b[ib]) {
      ia++;
    } else {
      ib++;
    }
  }

  return result;
}

int main()
{
  vector<int> a;
  vector<int> b;

  for(int i = 0; i < 100; i++) {
    a.push_back(i);
    b.push_back(100 - 2 * i);
  }

  vector<int> result = findCommon(a, b);
  for(int i = 0; i < result.size(); i++) {
    cout << result[i] << endl;
  }

  return 0;
}
