#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

void rotate(int** mx, int n) {
  for(int i = 0; i < n / 2; i++) {
    int first = i;
    int last = n - i - 1;
    for(int j = first; j < last; j++) {
      int offset = j - first;
      int top = mx[first][j];
      // left -> top
      mx[first][j] = mx[last - offset][first];
      // bottom -> left
      mx[last - offset][first] = mx[last][last - offset];
      // right -> bottom
      mx[last][last - offset] = mx[j][last];
      // top -> right
      mx[j][last] = top;
    }
  }
}

int main()
{
}
