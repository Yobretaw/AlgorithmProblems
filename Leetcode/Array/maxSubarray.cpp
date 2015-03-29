#include "iostream"
using namespace std;

int maxSubarray(int* a, int n) {
  int start        = 0;
  int max_start    = 0;
  int max_end      = 0;
  int max_so_far   = a[0];
  int max_end_here = a[0];
  bool allNegative = a[0] >= 0 ? false : true;

  for(int i = 1; i < n; i++) {
    if(max_end_here < 0) {
      max_end_here = a[i];
      start = i;
    } else {
      max_end_here += a[i];
    }

    if(max_end_here > max_so_far) {
      max_so_far = max_end_here;

      // update start and end indexes
      max_start = start;
      max_end = i;
    }

    if(a[i] > 0) {
      allNegative = false;
    }
  }

  if(allNegative) {
    return 0;
  }

  cout << "[" << max_start << ", " << max_end << "]" << endl;
  return max_so_far > 0 ? max_so_far : 0;
}


int main()
{
  int a[9] = {-2, 1, 2, 4, -1, 2, 1, -5, 4};
  cout << maxSubarray(a, 9) << endl;
  return 0;
}
