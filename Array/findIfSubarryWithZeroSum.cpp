#include "iostream"
#include "vector"
#include "map"
using namespace std;

bool find(vector<int> a) {
  if(a.size() == 0)
    return false;

  vector<int> s(a);
  map<int, bool> m;

  int sum = a[0];
  m[sum] = true;

  for(int i = 1; i < (int)a.size(); i++) {
    sum += a[i];

    if(m[sum]) {
      return true;
    }

    m[sum + a[i]] = true;
  }

  return false;
}

int main() {
  vector<int> a;
  a.push_back(4);
  a.push_back(2);
  a.push_back(-3);
  a.push_back(1);
  a.push_back(6);
  cout << find(a) << endl;
  return 0;
}
