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

/* 1 2       3 4       3 1
 * 3 4   --> 1 2   --> 4 2
 */
void rotate2(int** mx, int n) {
  for (int i = 0; i < n / 2; i++)
    for (int j = 0; j < n; j++)
      swap(mx[i][j], mx[n - 1 - i][j]);

  for(int i = 0; i < n; i++)
    for(int j = i + 1; j < n; j++)
      swap(mx[i][j], mx[j][i]);
}

int main()
{
  int** mx = new int*[10];
  for(int i = 0; i < 10; i++)
    mx[i] = new int[10];


  int count = 0;
  for(int i = 0; i < 10; i++) {
    for(int j = 0; j < 10; j++)
      mx[i][j] = count++;
  }

  for(int i = 0; i < 10; i++) {
    for(int j = 0; j < 10; j++) {
      cout << mx[i][j];
      if(mx[i][j] >= 10)
        cout << " ";
      else
        cout << "  ";
    }
    cout << endl;
  }
  rotate2(mx, 10);

  cout << endl;
  for(int i = 0; i < 10; i++) {
    for(int j = 0; j < 10; j++) {
      cout << mx[i][j];
      if(mx[i][j] >= 10)
        cout << " ";
      else
        cout << "  ";
    }
    cout << endl;
  }
}
