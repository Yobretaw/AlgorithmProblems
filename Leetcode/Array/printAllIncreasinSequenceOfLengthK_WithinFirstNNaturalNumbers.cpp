#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

void printSeq(const vector<int> vec) {
  for(int i = 0; i < vec.size(); ++i) {
    cout << vec[i];
    if(i != vec.size() - 1)
      cout << " ";
  }
  cout << endl;
}

void printHelp(int n, int k, int& len, vector<int>& curr) {
  if(len == k) {
    printSeq(curr);
    return;
  }

  int start = (len == 0) ? 1 : curr[len - 1] + 1;
  len++;

  while(start <= n) {
    curr[len - 1] = start;
    printHelp(n, k, len, curr);
    start++;
  }

  len--;
}

void print(int n, int k) {
  vector<int> curr(k);
  int len = 0;
  printHelp(n, k, len, curr);
}

int main()
{
  vector<int> curr;
  print(5, 3);
  return 0;
}
