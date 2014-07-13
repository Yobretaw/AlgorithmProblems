#include "iostream"
using namespace std;

// a is rotated from a sorted array
// this function return the min value of this array
int findMin(int* a, int n) {
  if(n == 0)
    return 0;

  if(n == 1)
    return a[0];

  int first = 0;
  int last = n - 1;

  while(first < last) {
    int mid = (first + last) / 2;

    if(a[mid] > a[last])
      first = mid + 1;
    else
      last = mid;
  }

  return a[first];
}

// a is a rotated array
// this function return the maximum value in the array
int findMax(int* a, int n) {
  if(n == 1)
    return a[0];

  int first = 0;
  int last = n - 1;
  
  while(first < last) {
    int mid = (first + last) / 2;

    if(a[mid] > a[last])
      first = mid;
    else
      last = mid - 1;
  }

  return a[first];
}

int main()
{
  int a[6] = { 4, 5, 6, 1, 2, 3 };
  cout << findMin(a, 6) << endl;
  cout << findMax(a, 6) << endl;
  return 0;
}
