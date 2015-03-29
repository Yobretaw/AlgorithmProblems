#include "iostream"
#include "vector"
#include "algorithm"
using namespace std;

int abs(int a) {
  return ( a < 0 ) ? -a : a;
}

int find(vector<int> a) {
  if(a.size() == 0) {
    return 0;
  }

  vector<int> s(a.size());
  s[0] = a[0];

  for(int i = 1; i < (int)a.size(); i++) {
    s[i] = s[i-1] + a[i];
  }

  sort(s.begin(), s.end());

  int min = 0;
  for(int i = 0; i < (int)s.size() - 1; i++) {
    int diff = abs(s[i + 1] - s[i]);
    min = diff < min ? diff : min;
  }

  return min;
}

int main() {
  vector<int> a;
  a.push_back(-3);
  a.push_back(1);
  a.push_back(4);
  a.push_back(-1);
  a.push_back(2);
  a.push_back(-4);
  a.push_back(9);
  a.push_back(0);
  a.push_back(-6);

  cout << find(a) << endl;
}
