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
 *  Determine whether an integer is a palindrome. Do this without extra space.
 *  
 *  Some hints:
 *  Could negative integers be palindromes? (ie, -1)
 *  
 *  If you are thinking of converting the integer to string, note the restriction of using extra space.
 *  
 *  You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
 *  you know that the reversed integer might overflow. How would you handle such case?
 *  
 *  There is a more generic way of solving this problem.
 */
bool isPalindrom(int x) {
  if(x < 0) return false;
  if(x < 10) return true;

  int d = 1;
  while(x / d >= 10) d *= 10;

  while(x > 0) {
    int q = x / d;
    int r = x % 10;

    if(q != r) return false;
    x = (x % d) / 10;
    d /= 100;
  }
  return true;
}

int main() {
  int x = 1234321;
  cout << isPalindrom(x) << endl;
  return 0;
}
