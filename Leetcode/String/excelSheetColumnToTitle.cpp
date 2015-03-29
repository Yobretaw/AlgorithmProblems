#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include "StringUtil.h"
#include <queue>
#include <unordered_map>
using namespace std;

string convertToTitle(int n) {
  return n == 0 ? "" : convertToTitle((n - 1) / 26) + (char)((n - 1) % 26 + 'A');
}

int main() {
  int a = 20000;
  for (int i = 1; i < a; ++i) {
    cout << i << " : " << convertToTitle(i) << endl;
  }
  return 0;
}
