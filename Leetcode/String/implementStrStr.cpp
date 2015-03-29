#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

/* Implement strStr(const char *str1, char *str2)
 *  - Returns a pointer to the first occurence of str2 in str1,
 *    or a null pointer if str2 is not part of str1
 *    
 *    str1 and str2 are '\0' ended
 */
char* strstr2(const char *str1, char *str2) {
  // if str2 is empty then return the full string
  if(!*str2) return (char*)str1;

  const char *p1;
  const char *p2;
  const char *p1_advance = str1;
  for(p2 = &str2[1]; *p2; ++p2)
    p1_advance++;   // advance p1_advance M-1 times

  for(p1 = str1; *p1_advance; p1_advance++) {
    char *p1_old = (char*)p1;
    p2 = str2;
    while(*p1 && *p2 && *p1 == *p2) {
      p1++;
      p2++;
    }

    // reach the end of p2(find a match point)
    if(!*p2) return p1_old;
    
    // current segement does not match, continue searching
    p1 = p1_old + 1;
  }

  return NULL;
}

int main() {
  char *str1 = (char*)"Man is least himself when talks in his own person";
  char *str2 = (char*)"talks in his own person";
  cout << strstr2(str1, str2)[0] << endl;
  return 0;
}
