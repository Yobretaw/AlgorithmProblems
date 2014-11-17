#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

bool isMember(string w, vector<string>& L) {
  for (int i = 0; i < L.size(); i++)
    if(w == L[i])
      return true;

  return false;
}

bool recognize(string w, vector<string>& L) {
  int n = w.length();
  if(n == 0)
    return isMember(w, L);

  vector<vector<int> > M(n, vector<int>(n));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      M[i][j] = false;
    }
  }

  for (int len = 1; len <= n; len++) {
    for (int start = 0; start < n - len + 1; start++) {
      int end = start + len - 1;

      for (int mid = start; mid < end; mid++) {
        if(M[start][mid] && M[mid + 1][end]) {
          M[start][end] = true;
          break;
        }
      }

      if(!M[start][end]) {
        M[start][end] = isMember(w.substr(start, end - start + 1), L);
      }
    }
  }
  return M[0][w.length() - 1];
}

int main() {
  vector<string> L = {
    "a", "ab", "abb"
  };

  string w = "abaaaaaabaabaaabbaa";
  cout << recognize(w, L) << endl;
  return 0;
}
