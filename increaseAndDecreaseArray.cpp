#include "iostream"
using namespace std;

int find(int* a, int n, int x) {
  int start = 0;
  int end = n-1;

  while(start < end) {
    cout << start << endl;
    cout << end << endl;
    int mid = (start + end) / 2;

    if(a[mid] > a[start])
      start = mid;
    else
      end = mid;
  }

  return start;
}



int main()
{
  int a[5] = { 1, 2, 3, 2, 1 };
  cout << find(a, 5, 1) << endl;
  return 0;
}
