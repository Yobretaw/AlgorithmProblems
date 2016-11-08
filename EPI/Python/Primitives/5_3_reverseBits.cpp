#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
#include <bitset>
using namespace std;

// Write a function that takes a 64-bit word x and returns a 64-bit word
// consisting of the bits of x in reverse order
unsigned long reverseBits(unsigned long x) {
  int low = 0, high = 63;
  while(low < high) {
    if(((x >> low) & 1) != ((x >> high) & 1))
      x ^= (1L << low) | (1L << high);

    low++;
    high--;
  }
  return x;
}

unsigned long reverseBits2(unsigned long x) {
  const int wordSize = 16;
  const int bitMask = 0xFFFF;

  // precomputed reverse for all 16-bit words
  int precomputed_reverse[65536];

  return precomputed_reverse[x & bitMask] << (3 * wordSize) |
         precomputed_reverse[(x >> wordSize) & bitMask] << (2 * wordSize) |
         precomputed_reverse[(x >> (2 * wordSize)) & bitMask] << wordSize |
         precomputed_reverse[(x >> (3 * wordSize)) & bitMask];
}

int main() {
  cout << bitset<64>(1) << endl;
  cout << bitset<64>(reverseBits(1)) << endl;
  return 0;
}
