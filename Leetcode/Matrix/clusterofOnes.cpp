#include "iostream"
#include "vector"
using namespace std;

void findHelp(vector<vector<int> >& m, int x, int y) {
  if(x < 0 || x >= (int)m.size() || y < 0 || y >= (int)m[0].size())
    return;

  if(m[x][y] == 0 || m[x][y] == 2)
    return;

  m[x][y] = 2;

  for(int i = -1; i <= 1; i++)
    for(int j = -1; j <= 1; j++)
      findHelp(m, x + i, y + j);
}

int find(vector<vector<int> >& m) {
  int count = 0;
  for(int i = 0; i < (int)m.size(); i++) {
    for(int j = 0; j < (int)m[0].size(); j++) {
      if(m[i][j] == 1) {
        count += 1;
        findHelp(m, i, j);
      }
    }
  }

  return count;
}

int main()
{
  vector<vector<int> > m;
  m.push_back(vector<int>());
  m.push_back(vector<int>());
  m.push_back(vector<int>());
  m.push_back(vector<int>());

  m[0].push_back(1);
  m[0].push_back(1);
  m[0].push_back(0);
  m[0].push_back(0);
  m[0].push_back(0);

  
  m[1].push_back(1);
  m[1].push_back(0);
  m[1].push_back(0);
  m[1].push_back(1);
  m[1].push_back(0);

  m[2].push_back(0);
  m[2].push_back(0);
  m[2].push_back(0);
  m[2].push_back(1);
  m[2].push_back(1);

  m[3].push_back(1);
  m[3].push_back(0);
  m[3].push_back(1);
  m[3].push_back(0);
  m[3].push_back(0);

  cout << find(m) << endl;
  for(int i = 0; i < (int)m.size(); i++) {
    for(int j = 0; j < (int)m[0].size(); j++) {
      if(m[i][j] == 2)
        m[i][j] = 1;
    }
  }
  return 0;
}
