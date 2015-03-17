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

/* 
 * The parity of a binary word is 1 if the number of 1s in the word is odd, otherwise it's 0.
 * For example, the parity of 1011 is 4, and the parity of 10001000 is 2.
 * 
 * How would you compute the parity of a very large set of 64-bit words?
 */
int parity(unsigned long x) {
  int result = 0;
  while(x) {
    result ^= (x & 1);
    x >>= 1;
  }
  return result;
}

// erase the lowest set bit in a word in a sinle operation: x & (x - 1),
// which can be used to improve the performance in the best and average
// case
int parity2(unsigned long x) {
  int result = 0;
  while(x) {
    result ^= 1;
    x &= (x - 1);
  }
  return result;
}

// If we want to test parities of a very large set of words, an excellent approach is to cache
// computation in a array-based look-up table. This solution exploits use of the fact that the
// XOR is associative.
int parity3(unsigned long x) {
  const int wordSize = 16;
  const int bitMask = 0xFFFF; // 1111 1111 1111 1111

  // assume precomputed_parity contains parities of all words with 16-bit
  int precomputed_parity[65536];

  return precomputed_parity[x >> (3 * wordSize)] ^
         precomputed_parity[(x >> (2 * wordSize)) & bitMask] ^
         precomputed_parity[(x >> wordSize) & bitMask] ^
         precomputed_parity[x & bitMask];
}

int parity4(unsigned int x) {
  x ^= x >> 32;
  x ^= x >> 16;
  x ^= x >> 8;
  x ^= x >> 4;
  x &= 0xF;   // only wants the last 4 bits of x

  // The LSB of fourBitParityLookupTable is the parit of 0,
  // next bit is parity of 1, followed by the parity of 2, etc.
  
  const int fourBitParityLookupTable = 0x6996;    // 0110100110010110

  return (fourBitParityLookupTable >> x) & 1;
}

int main() {
  cout << parity(11) << endl;
  cout << parity2(11) << endl;
  return 0;
}
