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
    int mid = first + (last - first) / 2;

    /**
     * Why check a[mid] > a[last] but not a[mid] > a[first]?
     *
     * Since there are two increasing inervals in the given array
     * and hence a[mid] > a[first] can have two cases:
     *
     * 1. both first and last are in the first increasing interval
     * 2. both first and last are in the second increasing interval
     * 
     * Therefore a[mid] > a[first] can be ambiguous. However there is
     * only one case where a[mid] > a[last]: first is in the first
     * increasing interval, and last is in the second increasing 
     * interval
     */
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
    int mid = first + (last - first) / 2;

    if(a[mid] > a[last])
      first = mid;
    else
      last = mid - 1;
  }

  return a[first];
}

/* a is a rotated array, find the index of target x */
int find(int* a, int n, int target) {
  if(n == 0)
    return -1;

  int start = 0;
  int end = n;
  while(start < end) {
    int mid = start + (end - start) / 2;
    if(target == a[mid])
      return mid;

    if(a[start] <= a[mid]) {
      if(a[start] <= target && target < a[mid])
        end = mid;
      else
        start = mid + 1;
    } else {
      if(a[mid] < target && target <= a[end - 1])
        start = mid + 1;
      else
        end = mid;
    }

    /* If allow duplicates, then following algorithm works */
    /*
    if(a[start] < a[mid]) {
      if(a[start] <= target && target < a[mid])
        end = mid;
      else
        start = mid + 1;
    } else if(a[start] > a[mid]){
      if(a[mid] < target && target <= a[end - 1])
        start = mid + 1;
      else
        end = mid;
    } else
      start++;
    */
  }
  return -1;
}

int main()
{
  int a[7] = { 4, 5, 6, 7, 1, 2, 3 };

  cout << "min: " << findMin(a, 7) << endl;
  cout << "max: " << findMax(a, 7) << endl;

  cout << find(a, 7, 4) << endl;
  cout << find(a, 7, 5) << endl;
  cout << find(a, 7, 6) << endl;
  cout << find(a, 7, 7) << endl;
  cout << find(a, 7, 1) << endl;
  cout << find(a, 7, 2) << endl;
  cout << find(a, 7, 3) << endl;
  
  return 0;
}
