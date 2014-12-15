#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

void mergeHelp(vector<int>& arr, int start, int end) {
  if( start == end )
    return;

  int mid = start + (end - start) / 2;

  mergeHelp(arr, start, mid);
  mergeHelp(arr, mid + 1, end);

  int i = start;
  int j = mid + 1;
  int tmp;

  while(i < mid + 1) {
    if(arr[i] > arr[j]) {
      swap(arr[i], arr[j]);

      tmp = j;
      while(arr[tmp] > arr[tmp + 1] && tmp < end) {
        swap(arr[tmp], arr[tmp + 1]);
        tmp++;
      }

      i++;
    }
  }
}

void mergesort(vector<int>& arr) {
  if(arr.size() == 1)
    return;

  mergeHelp(arr, 0, arr.size() - 1);
}

int main() {
  int size = 10;
  vector<int> arr(size);
  for(int i = 0; i < size; i++) {
    arr[i] = size - i;
  }

  mergesort(arr);
  for(int i = 0; i < arr.size(); i++) {
    cout << arr[i] << endl;
  }

  return 0;
}
