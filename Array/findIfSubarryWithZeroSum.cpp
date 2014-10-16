#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

void find(vector<int> a) {
  vector<int> s(a);
  
  for(unsigned i = 1; i < a.size(); ++i) {
    s[i] = s[i-1] + a[i];
  }

  unordered_map<int, int> m;
  for(unsigned i = 0; i < s.size(); ++i) {

    if(s[i] == 0) {
      cout << "[" << 0 << ", " << i << "]" << endl;
    }

    if(m.count(s[i]) == 1) {
      cout << "[" << m[s[i]] + 1 << ", " << i << "]" << endl;
    } else {
      m[s[i]] = i;
    }
  }
}


//bool find(vector<int> a) {
//  if(a.size() == 0)
//    return false;

//  vector<int> s(a);
//  map<int, bool> m;

//  int sum = a[0];
//  m[sum] = true;

//  for(int i = 1; i < (int)a.size(); i++) {
//    sum += a[i];

//    if(m[sum]) {
//      return true;
//    }

//    m[sum + a[i]] = true;
//  }

//  return false;
//}

int main() {
  vector<int> a;
  a.push_back(4);
  a.push_back(3);
  a.push_back(0);
  a.push_back(-3);
  a.push_back(0);
  a.push_back(3);
  a.push_back(-7);
  //find(a);
  
  sort(a.begin(), a.end());
  for(int i = 0; i < a.size(); i++) {
    cout << a[i] << endl;
  }
  
  return 0;
}
