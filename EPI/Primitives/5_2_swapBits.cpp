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

/* There are a number of ways in which bit manipulations can be accelerated. For
 * example, the expression x & (x - 1) equals x with the lowest set bit cleared,
 * and x & ~(x - 1) extract the LSB of x(all other bits are cleared).
 * 
 * Implement code that takes as input a 64-bit integer and swaps the bits in that
 * integer at index i and j from least significant bit.
 */
long swapBits(long x, int i, int j) {
  if(((x >> i) & 1) != ((x >> j) & 1))
    x ^= (1L << i) | (1L << j);

  return x;
}

int main() {
  return 0;
}
