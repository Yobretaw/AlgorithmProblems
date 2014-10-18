#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

void print(int n, int open = 0, int close = 0, string curr = "");

void print(int n, int open, int close, string curr) {
  if(close == n) {
    cout << curr << endl;
    return;
  }

  if(open < n) {
    print(n, open + 1, close, curr + '(');
  }

  if(open > close) {
    print(n, open, close + 1, curr + ')');
  }
}

int main()
{
  print(4);
  return 0;
}
