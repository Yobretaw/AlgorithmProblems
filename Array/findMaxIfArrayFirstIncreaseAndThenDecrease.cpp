#include <iostream>
using namespace std;

int find(int a[], int n);

int main() {
	int a[5] = { 21, 12, 10, 9, 1 };
	cout << find(a, 5) << endl;
	return 0;
}

int find(int a[], int n) {
  if( n == 1 )
    return a[0];
    
  int first = 0;
  int end = n - 1;

  while(first < end) {
    int mid = (first + end) / 2;

    if(mid == 0)
      return ( a[0] > a[1] )? a[0] : a[1];
    if(mid == n - 1)
      return ( a[n - 1] > a[n - 2] )? a[n - 1] : a[n - 2];

    // a[mid] is the maximum value
    if(a[mid] > a[mid + 1] && a[mid] > a[mid - 1])
      return mid;

    if(a[mid] > a[mid + 1] && a[mid] < a[mid-1])
      end = mid;
    else if(a[mid] < a[mid + 1] && a[mid] > a[mid - 1])
      first = mid + 1;
  }
  return first;
}
