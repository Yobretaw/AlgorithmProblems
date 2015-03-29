#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <climits>
#include <unordered_map>
using namespace std;

bool canMakeChangeHelp(const vector<int>& dom, int total, unordered_map<int, bool>& seen);
vector<int> coinChangeHelp(const vector<int>& dom, int total, unordered_map<int, vector<int> >& seen);

vector<int> coinChangeHelp(const vector<int>& dom, int total, unordered_map<int, vector<int> >& seen) {
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
      curr = coinChangeHelp(dom, rest, seen);
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

// return the optimal combination to make change of amount total
vector<int> coinChange(const vector<int>& dom, int total) {
  unordered_map<int, vector<int> > seen;
  return coinChangeHelp(dom, total, seen);
}



// return true we can make change for the given 'total'
// no need to find the optimal changing combination
bool canMakeChange(const vector<int>& dom, int total) {
  unordered_map<int, bool> seen;
  return canMakeChangeHelp(dom, total, seen);
}


bool canMakeChangeHelp(const vector<int>& dom, int total, unordered_map<int, bool>& seen) {
  for (int i = 0; i < dom.size(); i++) {
    if(dom[i] == total) {
      return true;
    }
  }

  // assume dom is sorted
  if(total < dom[0])
    return false;

  for (int i = 0; i < dom.size(); i++) {
    if(seen.count(total) == 0 && canMakeChangeHelp(dom, total - dom[i], seen)) {
      return true;
    }

    seen[total] = 1;
  }

  return false;
}

int main()
{
  vector<int> dom;
  dom.push_back(3);
  dom.push_back(5);
  dom.push_back(18);
  dom.push_back(25);
 
  cout << canMakeChange(dom, 16) << endl;
  vector<int> result = coinChange(dom, 17);
  //for(int i = 0; i < result.size(); i++) {
  //  cout << result[i] << endl;
  //}

  return 0;
}
