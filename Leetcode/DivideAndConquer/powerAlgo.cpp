#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
using namespace std;

// calculate x^n
// x^n = x^(n/2) * x^(n/2) * x^(n % 2)

double powHelp(double x, int n) {
  if(n == 0) return 1;
  if(n == 1) return x;

  double half = pow(x, n / 2);
  double rest = pow(x, n % 2);

  return half * half * rest;
}

double pow(double x, int n) {
  return n < 0 ? 1.0 / powHelp(x, -n) : powHelp(x, n);
}

int main() {
  cout << pow(8, 3) << endl;
  return 0;
}
