#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

/*
 * Create a bit mask from start bit to end bit
 */
unsigned int mask(unsigned int start, unsigned int end) {
  unsigned int bits = ( 1 << (end - start + 1) ) - 1;
  return bits << start;
}

int main()
{
  cout << mask(3, 5) << endl;
  return 0;
}
