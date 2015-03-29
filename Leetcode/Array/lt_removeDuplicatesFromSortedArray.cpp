#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

/* Given a sorted array, remove the duplicates in place
 * such that each element appear only once and return
 * the new length
 * 
 * Do not allocate extra space for another array, do this IN PLACE
 *
 * input: arr = [1, 1, 2]
 * return: length: 2, and arr is now [1, 2]
 */
int removeDup(int arr[], int n) {
  if(n == 0)
    return 0;

  int index = 1;
  for(int i = 1; i < n; i++) {
    if(arr[i] != arr[i-1]) {
      arr[index++] = arr[i];
    }
  }

  return index;
}

/* Follow up for "Remove Duplicates": What if duplicates are
 * allowed at most twice ?
 * 
 * in: A = [1, 1, 1, 2, 2, 3]
 * out: len = 5 and A = [1, 1, 2, 2, 3]
 */
int removeDupAllowTwo(int arr[], int n) {
  if(n <= 2)
    return n;

  int index = 2;

  for(int i = 2; i < n; i++) {
    if(arr[i] != arr[i-2]) {
      arr[index++] = arr[i];
    }
  }

  return index;
}

/* Now array is unsorted, remove duplicates and allow k times 
 */
int removeDupAllowTwo_unsorted(int arr[], int n, int k) {
  if(n == 0)
    return 0;

  int index = 0;
  unordered_map<int, int> seen;
  for(int i = 0; i < n; i++) {
    if(seen.count(arr[i]) != 0 && seen[arr[i]] < k) {
      arr[index++] = arr[i];
      seen[arr[i]]++;
    } else if(seen.count(arr[i]) == 0){
      arr[index++] = arr[i];
      seen[arr[i]] = 1;
    }
  }

  return index;
}

int main() {
  int a[] = {1, 1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 7, 7};
  //int len = removeDup(a, 13);
  //int len = removeDupAllowTwo(a, 13);
  int len = removeDupAllowTwo_unsorted(a, 13, 2);
  for(int i = 0; i < len; i++)
    cout << a[i] << endl;
  return 0;
}
