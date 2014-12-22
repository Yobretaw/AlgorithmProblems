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

  int idx = 0;
  vector<int> tmp(end - start + 1);
  while( i <= mid && j <= end ) {
    tmp[idx++] = (arr[i] < arr[j]) ? arr[i++] : arr[j++];
  }
  while(i <= mid) {
    tmp[idx++] = arr[i++];
  }
  while(j <= end) {
    tmp[idx++] = arr[j++];
  }

  for(int i = 0; i < idx; i++) {
    arr[start + i] = tmp[i];
  }
}

void mergesort(vector<int>& arr) {
  if(arr.size() == 1)
    return;

  mergeHelp(arr, 0, arr.size() - 1);
}

int main() {
  int size = 2000;
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
