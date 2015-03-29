#include "iostream"
using namespace std;

int partition(int* a, int start, int end) {
  int pivot = a[end];

  while(start < end) {
    while(a[start] < pivot)
      start++;

    while(a[end] > pivot)
      end--;

    if(a[start] == a[end])
      start++;
    else if(start < end) {
      int tmp = a[start];
      a[start] = a[end];
      a[end] = tmp;
    }
  }

  return end;
}

int select(int* a, int start, int end, int k) {
  if(start == end)
    return a[start];
  else {
    int j = partition(a, start, end);
    if(j == k) return a[j];
    if(j > k)
      return select(a, start, j-1, k);
    else
      return select(a, j+1, end, k-j);
  }
}

int main()
{
  int a[] = {4, 2, 2, 5, 0, 3, 5, 6, 7 };
  int sortedA[] = {0, 2, 2, 3, 4, 5, 5, 6, 7};
  //int a[] = { 2, 8, 1, 8, 1, 7, 9, 2, 7 };
//int a[] = {1, 1, 2, 2, 7, 7, 8, 8, 9};
  for(int i = 0; i < 8; i++) {
     cout << (select(a, 0, 8, i) == sortedA[i])  << endl;
  }

  return 0;
}
