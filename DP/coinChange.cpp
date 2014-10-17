#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <climits>
#include <unordered_map>
using namespace std;

vector<int> coinChange(const vector<int>& dom, int total, unordered_map<int, vector<int> >& seen) {
  vector<int> result;
  for(int i = 0; i < dom.size(); i++) {
    if(total == dom[i]) {
      result.push_back(dom[i]);
      return result;
    }
  }

  int min = INT_MAX;
  int d = -1;
  for(int i = 0; i < dom.size(); i++) {
    if(total < dom[i])
      continue;

    int rest = total - dom[i];
    vector<int> curr;
    
    if(seen.count(rest) == 0) {
      curr = coinChange(dom, rest, seen);
      seen[rest] = curr;
    } else {
      curr = seen[rest];
    }

    if(curr.size() != 0 && curr.size() < min) {
      d = i;
      min = curr.size();
      result = curr;
    }
  }
  
  if(d != -1)
    result.push_back(dom[d]);

  return result;
}


int main()
{
  vector<int> dom;
  dom.push_back(2);
  dom.push_back(5);
  dom.push_back(18);
  dom.push_back(25);
 
  unordered_map<int, vector<int> > seen;
  vector<int> result = coinChange(dom, 32, seen);
  for(int i = 0; i < result.size(); i++) {
    cout << result[i] << endl;
  }

  return 0;
}
