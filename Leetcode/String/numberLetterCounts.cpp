#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

/* If the numbers 1 to 5 are written out in words: one,
 * two, three, four, five, then there are 3 + 3 + 5 + 4
 * + 4 = 19 letters used in total.
 *
 * If all the numbers from 1 to 1000 (one thousand) 
 * inclusive were written out in words, how many letters
 * would be used?
 * 
 * NOTE: Do not count spaces or hyphens. For example,
 * 342 (three hundred and forty-two) contains 23 letters
 * and 115 (one hundred and fifteen) contains 20 letters.
 * The use of "and" when writing out numbers is in
 * compliance with British usage.
 */
int count1k() {
  static vector<string> num = {
    "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen"
  };

  static vector<string> tens = {
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
    "hundred"
  };

  vector<string> result;
  for (int i = 1; i <= 999; ++i) {
    int curr = i;
    int hundreds = curr / 100;
    if(hundreds > 0) {
      result.push_back((num[hundreds - 1] + tens[8]));

      if((curr % 100) > 0) result.push_back("and");
    }

    curr %= 100;

    int ten = curr / 10;
    if(ten >= 2) {
      result.push_back(tens[ten - 2]);
      curr %= 10;

      if(curr > 0) {
        result.push_back(num[curr - 1]);
      }
    } else {
      // ten == 0 or 1
      result.push_back(num[curr - 1]);
    }
  }

  result.push_back("onethousand");

  int len = 0;
  for (int i = 0; i < result.size(); ++i) {
    len += result[i].length();
  }
  return len;
}

int main() {
  cout << count1k() << endl;
  return 0;
}
