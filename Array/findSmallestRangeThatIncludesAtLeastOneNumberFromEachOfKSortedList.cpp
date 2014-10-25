#include <iostream>
#include <climits>
#include <queue>
#include <vector>
#include <stack>
#include <unordered_map>
using namespace std;

struct compare {
  // for min heap
  bool operator()(const int& l, const int& r) {
    return l > r;
  }
};

// reverse all lists in the given list of lists
void reverseAllList(vector<vector<int> >& list) {
  for(int i = 0; i < (int)list.size(); ++i) {
    vector<int> tmp;
    vector<int> curr = list[i];

    for(int j = curr.size() - 1; j >= 0; --j) {
      tmp.push_back(curr[j]);
    }

    list[i] = tmp;
  }
}

void printSmallestRange(vector<vector<int> > list) {
  int lower = INT_MAX;
  int upper = INT_MIN;

  int l = lower;
  int u = upper;
  int range = INT_MAX;
  priority_queue<int, vector<int>, compare> pq;
  unordered_map<int, int> m;

  // first reversr all list
  reverseAllList(list);

  // insert the first value of the list into the heap
  for(int i = 0; i < (int)list.size(); i++) {
    int val = list[i].back();
    list[i].pop_back();

    if(val < lower)
      lower = val;
    if(val > upper)
      upper = val;

    pq.push(val);
    m[val] = i;
  }

  l = lower;
  u = upper;
  range = u - l;

  while(true) {

    int listIndex = m[pq.top()];
    pq.pop();

    // if one list has no elements, then break;
    if(list[listIndex].size() == 0)
      break;

    int nextVal = list[listIndex].back();
    list[listIndex].pop_back();
    pq.push(nextVal);

    if(lower < pq.top()) {
      lower = pq.top();
    }
    
    if(nextVal > upper) {
      upper = nextVal;
    }

    if((upper - lower) < range) {
      u = upper;
      l = lower;
      range = u - l;
    }

    m[nextVal] = listIndex;
  }

  cout << "The minimum range is : [" << l << ", " << u << "]" << endl;

  return;
}

int main() {
  vector<vector<int> > list;
  list.push_back(vector<int>());
  list.push_back(vector<int>());
  list.push_back(vector<int>());

  list[0].push_back(4);
  list[0].push_back(10);
  list[0].push_back(15);
  list[0].push_back(24);
  list[0].push_back(26);

  list[1].push_back(0);
  list[1].push_back(9);
  list[1].push_back(12);
  list[1].push_back(20);
  list[1].push_back(21);

  list[2].push_back(5);
  list[2].push_back(18);
  list[2].push_back(22);
  list[2].push_back(30);

  printSmallestRange(list);
  return 0;
}



void printSmallestRangeOfTwoSortedList(vector<int>& a, vector<int>& b) {
  if(a.size() == 0 || b.size() == 0) {
    return;
  }

  stack<int> sa, sb;
  for (int i = a.size() - 1; i >= 0; --i)
    sa.push(a[i]);
  for (int i = b.size() - 1; i >= 0; --i)
    sb.push(b[i]);

  int lower = min(sa.top(), sb.top());
  int upper = max(sa.top(), sb.top());
  if(lower == upper) {
    cout << "[" << lower << ", " << upper <<  "]";
    return;
  }

  sa.pop();
  sb.pop();


}
