#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <unordered_map>
using namespace std;


// The 3SUM problem asks if a given set of n integers, each with absolute value bounded by some polynomial in n, contains three elements that sum to zero.
void threeSum(vector<int> a) {
  unordered_map<int, int> m;
  for(int i = 0; i < a.size(); ++i) {
    m[a[i]] = i;
  }

  for(int i = 0; i < a.size() - 1; ++i) {
    for(int j = i + 1; j < a.size(); ++j) {
      int val = -(a[i] + a[j]);
      if(m.count(val) == 1 && m[val] < i && i < j) {
        cout << m[val] << " " << i << " " << j << endl;
      }
    }
  }
}

int main()
{
  vector<int> a;
  a.push_back(-25);
  a.push_back(-10);
  a.push_back(-7);
  a.push_back(-3);
  a.push_back(2);
  a.push_back(4);
  a.push_back(8);
  a.push_back(10);

  threeSum(a);
  return 0;
}
