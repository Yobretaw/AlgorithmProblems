#include "iostream"
#include "string"
using namespace std;

bool isInterleaved(string a, string b, string c) {
  if(a.length() + b.length() != c.length())
    return false;

  int m = a.length();
  int n = b.length();
  bool IL[m+1][n+1];
  memset(IL, 0, sizeof(IL));

  for(int i = 0; i < m+1; i++) {
    for(int j = 0; j < n+1; j++) {
      if(i == 0 && j == 0)
        IL[i][j] = true;

      else if(i == 0 && b[j-1] == c[j-1])
        IL[i][j] = IL[i][j-1];

      else if(j == 0 && a[i-1] == c[i-1])
        IL[i][j] = IL[i-1][j];

      else if(a[i-1] == c[i+j-1] && b[j-1] != c[i+j-1])
        IL[i][j] = IL[i-1][j];

      else if(a[i-1] != c[i+j-1] && b[j-1] == c[i+j-1])
        IL[i][j] = IL[i][j-1];

      else if(a[i-1] == c[i+j-1] && b[j-1] == c[i+j-1])
        IL[i][j] = (IL[i][j-1] || IL[i-1][j]);
    }
  }


  for(int i = 0; i < m+1; i++) {
    for(int j = 0; j < n+1; j++) {
      cout << IL[i][j] << " ";
    }
    cout << endl;
  }


  return IL[m][n];
}

int main()
{
  string a = "XYZX";
  string b = "ZXYS";
  string c = "XZYXZYXS";
  cout << isInterleaved(a, b, c) << endl;
  return 0;
}
