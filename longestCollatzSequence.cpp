#include "iostream"
using namespace std;

int test();
int lcs();

int main()
{
  cout << lcs() << endl;
  return 0;
}


int lcs() {
  int i = 2;
  int size = 10000000;
  int max = 0;
  int m = 0;

  for (i = 113383; i < size; ++i)
  {
    int c = 0;
    int count = 0;
    unsigned long long curr = i;
    while(curr != 1 ) {
      curr = (curr % 2 == 0)? curr/2 : 3*curr+1;
      count++;
      c++;
    }
    if (count > max)
    {
      max = count;
      m = i;
    }
  }

  return m;
}
