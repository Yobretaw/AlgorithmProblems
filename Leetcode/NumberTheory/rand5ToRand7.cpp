#include "iostream"
#include <stdlib.h>
#include "cstdlib"
#include "time.h"
using namespace std;

int rand5() {
  return rand() % 5 + 1;
}

// number of call to rand5():
// S = 1 * 4/5 + 2 * 1/5 * 4/5 + 3 * (1/5)^2 * 4/5 + ...
//   = 4/5*(1/5 + 2/25 + 3/125 + 4/625 + ...)
// =>
// 1/5*S  = 1/25 + 2/125 + 3/625 + ...
// =>
// 4/5*S = 1/5 + 1/5 + 1/5 + .... = 1/(1-1/5) = 5/4
// => S = 25 / 16 = 1.5625
// 
// So on average a call to genZeroOrOne will call rand5() 1.25 times
int genZeroOrOne() {
  int ret = rand5();
  while(ret == 1)
    ret = rand5();

  return ret % 2;
}

int rand7_help() {
  int result = 0;

  result |= genZeroOrOne() == 0 ? 1 : 0;
  result |= genZeroOrOne() == 0 ? 2 : 0;
  result |= genZeroOrOne() == 0 ? 4 : 0;

  return result;
}

// Similar to genZeroOrOne, every call to rand7() will call
// rand7_help (7/6)^2 = 49/36 times
// Therefore every call to rand7() will call rand5 25/16 * 49/36 = 2.126 times
int rand7() {
  int result = rand7_help();
  while(result == 0)
    result = rand7_help();

  return result;
}

int main()
{
  srand(time(NULL));
  int a[1000000] = {0};

  for(int i = 0; i < 1000000; i++) {
    a[i] = rand7();
  }

  int b[7] = {0};

  for(int i = 0; i < 1000000; i++) {
    b[a[i]-1]++;
  }

  for(int i = 0; i < 7; i++) {
    double pos = (double)b[i] / 1000000;
    cout << i + 1 << " : " << pos << "| " << (pos - (double)1/7) << endl;
  }
  return 0;
}
