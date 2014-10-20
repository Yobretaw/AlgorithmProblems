#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

void find(vector<int> a) {
  vector<int> s(a);
  
  for(int i = 1; i < a.size(); ++i) {
    s[i] = s[i-1] + a[i];
  }

  unordered_map<int, vector<int> > m;
  for(int i = 0; i < s.size(); ++i) {
    if(a[i] == 0) {
      cout << "[" << i << ", " << i << "]" << endl;
    }

    if(s[i] == 0 && i != 0) {
      cout << "[" << 0 << ", " << i << "]" << endl;
    }

    if(m.count(s[i]) == 1) {
      for(int j = 0; j < m[s[i]].size(); ++j) {
        int next = m[s[i]][j] + 1;
        if(next == i) continue;
        cout << "[" << next << ", " << i << "]" << endl;
      }
    }

    m[s[i]].push_back(i);
  }
}

int main() {
  vector<int> a;
  //a.push_back(0);
  //a.push_back(0);
  //a.push_back(0);
  //a.push_back(0);
  //a.push_back(0);
  //a.push_back(0);
  //a.push_back(0);
  //a.push_back(0);

  a.push_back(0);
  a.push_back(1);
  a.push_back(-1);
  a.push_back(0);

  a.push_back(4);
  a.push_back(3);
  a.push_back(0);
  a.push_back(-3);
  a.push_back(0);
  a.push_back(3);
  a.push_back(-7);
  find(a);
  
  return 0;
}
