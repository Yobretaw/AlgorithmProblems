#include "iostream"
#include "vector"
using namespace std;

vector<vector<int> > findRow(vector<vector<int> > m) {
  vector<vector<int> > result((int)m.size());

  int mx = (int)m.size();
  int my = (int)m[0].size();

  for(int i = 0; i < mx; i++) {
    result[i] = vector<int>(my);

    vector<int> lr(my);
    lr[0] = m[i][0];

    for(int j = 1; j < my; j++) {
      lr[j] = ( m[i][j] > m[i][j-1] ) ? m[i][j] : m[i][j-1];
    }


    vector<int> rl(my);
    rl[my-1] = m[i][my-1];


    for(int j = my-2; j >= 0; j--) {
      rl[j] = ( m[i][j] > m[i][j+1] ) ? m[i][j] : m[i][j+1];
    }

    for(int j = 0; j < my; j++) {
      result[i][j] = min(lr[j], rl[j]);
    }

  }

  return result;
}


vector<vector<int> > findCol(vector<vector<int> > m) {
  vector<vector<int> > result((int)m.size());

  int mx = (int)m.size();
  int my = (int)m[0].size();

  for(int i = 0; i < my; i++) {
    result[i] = vector<int>(mx);

    vector<int> lr(mx);
    lr[0] = m[0][i];

    for(int j = 1; j < mx; j++) {
      lr[j] = ( m[j][i] > m[j-1][i] ) ? m[j][i] : m[j-1][i];
    }

    vector<int> rl(mx);
    rl[mx-1] = m[mx-1][i];
    
    for(int j = mx-2; j >=0; j--) {
      rl[j] = ( m[j][i] > m[j+1][i] ) ? m[j][i] : m[j+1][i];
    }

    for(int j = 0; j < mx; j++) {
      result[i][j] = min(lr[j], rl[j]);
    }
  }

  return result;
}


int calc(vector<vector<int> > m) {
  vector<vector<int> > rowMax = findRow(m);
  vector<vector<int> > colMax = findCol(m);

  int mx = (int)m.size();
  int my = (int)m[0].size();

  int total = 0;

  for(int i = 0; i < mx; i++) {
    for(int j = 0; j < my; j++) {
      int sum = min(rowMax[i][j], colMax[i][j]) - m[i][j];
      if(sum < 0)
        continue;

      total += sum;
    }
  }

  return total;
}


int main()
{
  vector<vector<int> > m;
  for(int i = 0; i < 4; i++)
    m.push_back(vector<int>());

  m[0].push_back(1);
  m[0].push_back(1);
  m[0].push_back(2);
  m[0].push_back(1);
  
  m[1].push_back(1);
  m[1].push_back(2);
  m[1].push_back(3);
  m[1].push_back(1);

  m[2].push_back(2);
  m[2].push_back(4);
  m[2].push_back(1);
  m[2].push_back(3);

  m[3].push_back(4);
  m[3].push_back(1);
  m[3].push_back(2);
  m[3].push_back(4);

  cout << calc(m) << endl;
  return 0;
}
