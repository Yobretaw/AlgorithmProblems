#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

int findMaj(const vector<int>& arr) {
  int majIdx = 0, count = 1;
  for (int i = 1; i < arr.size(); i++) {
    if(arr[majIdx] == arr[i])
      count++;
    else
      count--;

    if(count == 0) {
      majIdx = i;
      count = 1;
    }
  }

  return arr[majIdx];
}

int main() {
  vector<int> arr = { 3, 3, 4, 2, 4, 4, 2, 4, 4 };
  cout << findMaj(arr) << endl;
  return 0;
}
