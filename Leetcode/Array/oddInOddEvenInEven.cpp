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
 *                                    奇数位上都是奇数或者偶数位上都是偶数
 *
 * 给定一个长度不小于2的数组arr。 写一个函数调整arr，使arr中要么所有的偶数位上都是偶数，要么所有的奇数位上都是奇数上。
 * 要求：如果数组长度为N，时间复杂度请达到O(N)，额外空间复杂度请达到O(1),下标0,2,4,6...算作偶数位,下标1,3,5,7...算作奇数位，
 * 例如[1,2,3,4]调整为[2,1,4,3]即可
 */
void convert(vector<int>& arr) {
  int len = arr.size();

  if(len == 0 || len == 1) return;

  int evenIdx = 0, oddIdx = 1;
  while(evenIdx < len && oddIdx < len) {
    bool isEven = arr[evenIdx] % 2 == 0;
    bool isOdd = arr[oddIdx] % 2 == 1;

    if(isEven && isOdd) {
      evenIdx += 2;
      oddIdx += 2;
    } else if(isEven || isOdd) {
      if(!isEven) {
        while(oddIdx < len && arr[oddIdx] % 2 == 1) oddIdx +=2;
        if(oddIdx >= len) break;
        swap(arr[evenIdx], arr[oddIdx]);
      } else {
        while(evenIdx < len && arr[evenIdx] % 2 == 0) evenIdx +=2;
        if(evenIdx >= len) break;
        swap(arr[evenIdx], arr[oddIdx]);
      }
    } else {
      swap(arr[evenIdx], arr[oddIdx]);
      evenIdx += 2;
      oddIdx += 2;
    }
  }
}

/*
 *  Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead
 *  of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three
 *  and five print “FizzBuzz”.
 */
void fizzbuzz() {
  string fizz = "Fizz";
  string buzz = "Buzz";

  for(int i = 1; i < 100; ++i) {
    if(i % 3 == 0 && i % 5 == 0) cout << fizz + buzz << endl;
    else if(i % 3 == 0) cout << fizz << endl;
    else if(i % 3 == 0) cout << buzz << endl;
    else cout << i << endl;
  }
}

int main() {
  //vector<int> arr;
  //int size = 20;
  //for(int i = 0; i < size; ++i) arr.push_back(i + 1);
  //convert(arr);
  //for(auto v : arr) cout << v << " ";
  //cout << endl;
  fizzbuzz();
  return 0;
}
