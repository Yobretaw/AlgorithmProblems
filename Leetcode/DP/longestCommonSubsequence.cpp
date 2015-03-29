#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

vector<vector<int> > buildTable(const string& a, const string& b) {
  vector<vector<int> > table(a.length());
  for(int i = 0; i < a.length(); ++i) {
    table[i] = vector<int>(b.length(), 0);
  }

  for(int i = 1; i < table.size(); i++) {
    for(int j = 1; j < table[i].size(); j++) {
      if(i == 0 || j == 0)
        continue;

      if(a[i] == b[j])
        table[i][j] = table[i-1][j-1] + 1;
      else
        table[i][j] = max(table[i-1][j], table[i][j-1]);
    }
  }

  return table;
}

string lcs(const string& a, const string& b) {
  vector<vector<int> > table = buildTable(a, b);

  int max_x = 0;
  int max_y = 0;
  int max_len = 0;

  for(int i = 0; i < table.size(); i++) {
    for(int j = 0; j < table[i].size(); j++) {
      if(table[i][j] > max_len) {
        max_x = i;
        max_y = j;
      }
    }
  }

  string res;
  while(max_x != 0 && max_y != 0) {
    if(table[max_x][max_y] > max(table[max_x-1][max_y], table[max_x][max_y-1])) {
      res = a[max_x--] + res;
      continue;
    }

    if(table[max_x-1][max_y] > table[max_x][max_y-1])
      max_x--;
    else
      max_y--;
  }

  return res;
}

int main() {
  string a = "algorithm";
  string b = "exploration";
  cout << lcs(a, b) << endl;
  return 0;
}
