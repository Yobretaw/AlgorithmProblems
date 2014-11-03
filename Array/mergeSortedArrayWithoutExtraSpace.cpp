#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;
/* ZH:
 *
 * 有2个长度为n和m的有序的整型数组arr1和arr2，请将他们合并为一个n+m的有序数组。

注意：数组arr1包含足够的空间存放下n+m个元素，请直接将结果合并到数组arr1中。

提示：不要使用任何辅助数组，辅助空间。

样例：

n=3
m=2
arr1: [1,4,8,x,x]
arr2: [-1,5]

算法运行后arr1应该为[-1,1,4,5,8]

*/

void merge(vector<int>& a, vector<int>& b, int m, int n) {
  m--;
  n--;
  for (int i = m + n + 1; i >= 0; i--) {
    if(n < 0 || (m >= 0 && a[m] > b[n])) {
      a[i] = a[m--];
    } else {
      a[i] = b[n--];
    }
  }
}

int main()
{
  vector<int> a = {1, 4, 8, -1, -1, -1};
  vector<int> b = {-1, 3, 5};

  merge(a, b, 3, 3);
  for (int i = 0; i < a.size(); i++) {
    cout << a[i] << endl;
  }
  return 0;
}
