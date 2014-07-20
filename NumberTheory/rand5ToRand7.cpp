#include "iostream"
#include <stdlib.h>
#include "cstdlib"
#include "time.h"
using namespace std;

int rand5() {
  return rand() % 5 + 1;
}

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
