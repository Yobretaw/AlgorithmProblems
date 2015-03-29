#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

int count(vector<vector<int> >& m, int x, int y) {
  int row = m[0].size();
  int col = m.size();

  // lower right corner
  if(x == row - 1 && y == col - 1)
    return m[x][y];

  // no path from here
  if(x == row || y == col || m[x][y] == 0)
    return 0;

  // go right or bottom
  return count(m, x+1, y) + count(m, x, y+1);
}

int countHelp(vector<vector<int> > & m) {
  return count(m, 0, 0);
}

int main() {

  vector<vector<int> > m0 = {
    {1, 1, 1, 0},
    {1, 1, 0, 1},
    {1, 0, 1, 1},
    {0, 1, 1, 1}
  };

  vector<vector<int> > m1 = {
    {1, 1, 1, 1},
    {1, 1, 0, 1},
    {1, 0, 1, 1},
    {0, 1, 1, 1}
  };

  vector<vector<int> > m2 = {
    {1, 1, 1, 1},
    {1, 1, 1, 1},
    {1, 0, 1, 1},
    {0, 1, 1, 1}
  };

  vector<vector<int> > m3 = {
    {1, 1, 1, 1},
    {1, 1, 1, 1},
    {1, 1, 1, 1},
    {0, 1, 1, 1}
  };
  
  vector<vector<int> > m4 = {
    {1, 1, 1, 1},
    {1, 1, 1, 1},
    {1, 1, 1, 1},
    {1, 1, 1, 1}
  };
  
  vector<vector<int> > m5 = {
    {1, 1, 1, 1},
    {1, 1, 1, 1},
    {1, 1, 1, 1},
    {1, 1, 1, 0}
  };
  
  vector<vector<int> > m6 = {
    {0, 1, 1, 1},
    {1, 1, 1, 1},
    {1, 1, 1, 1},
    {1, 1, 1, 0}
  };

  cout << countHelp(m0) << endl;
  cout << countHelp(m1) << endl;
  cout << countHelp(m2) << endl;
  cout << countHelp(m3) << endl;
  cout << countHelp(m4) << endl;
  cout << countHelp(m5) << endl;
  cout << countHelp(m6) << endl;
  return 0;
}
