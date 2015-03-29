#include "iostream"
#include "vector"
using namespace std;

// Given three arrays sorted in non-decreasing order, print all common elements in these ways
void find(vector<int> a, vector<int> b, vector<int> c) {
  int la = a.size();
  int lb = b.size();
  int lc = c.size();

  int x = 0;
  int y = 0;
  int z = 0;

  while(x < la && y < lb && z < lc) {
    if(a[x] == b[y] && b[y] == c[z]) {
      cout << a[x] << " " << endl;

      x++;
      y++;
      z++;
    } else if(a[x] < b[y]) {
      x++;
    } else if(b[y] < c[z]) {
      y++;
    } else {
      z++;
    }
  }
}


int main() {
  
  return 0;
}
