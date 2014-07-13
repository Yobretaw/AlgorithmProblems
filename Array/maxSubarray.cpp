#include "iostream"
using namespace std;

int maxSubarray(int* a, int n) {
  int max_so_far = a[0];
  int max_end_here = a[0];

  for(int i = 1; i < n; i++) {
    if(max_end_here < 0)
      max_end_here = a[i];
    else
      max_end_here += a[i];

    if(max_end_here > max_so_far)
      max_so_far = max_end_here;
  }

  return max_so_far > 0 ? max_so_far : 0;
}


int main()
{
  int a[9] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
  cout << maxSubarray(a, 9) << endl;
  return 0;
}
