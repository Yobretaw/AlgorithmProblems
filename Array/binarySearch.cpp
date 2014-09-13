#include "iostream"
using namespace std;

// given a sorted array a of length n and an integer x
// return the position of x in a
int search(int* a, int n, int x) {
  int first = 0;
  int last = n - 1;

  while(first <= last) {
    int mid = (first + last) / 2;

    if(a[mid] == x)
      return mid;

    // Q: why increment lower boound but not decrement upper bound?
    // A: Since mid = (first + last) / 2 always rounds to its follor.
    // Consider if a = [1, 2, 3] and x = 3
    // In first iteration we have mid = (0 + 2)/2 = 1, and a[1] = 1
    // Then if we decrement `last`, last is now 2 - 1 = 1, and a[2] will
    // never be hit.
    if(a[mid] < x)
      first = mid + 1;
    else
      last = mid;
  }

  return -1;
}

int main()
{
  int a[5] = { 1, 2, 3, 4, 5 };
  cout << search(a, 5, 1) << endl;
  cout << search(a, 5, 2) << endl;
  cout << search(a, 5, 3) << endl;
  cout << search(a, 5, 4) << endl;
  cout << search(a, 5, 5) << endl;
  return 0;
}
