/*
 * Given a array of integers where each entry represents the height of the wall
 * Now imagine it rains. How much water is going to be accumulated in puddles 
 * between walls?
 */
#include <iostream>
#include <utility>
#include <stack>
using namespace std;

int calVolume(int* land, int length);
int calVolume_stack(int* land, int length);

int main()
{
  int a[9] = {2, 5, 1, 2, 3, 4, 7, 7, 6};
  int b[12] = {2, 3, 5, 1, 2, 1, 3, 1, 9, 2, 7, 2};
  int c[12] = {9, 8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8};

  cout << calVolume(a, 9) << endl;            // should output 10
  cout << calVolume_stack(a, 9) << endl;      // should output 10

  cout << calVolume(b, 12) << endl;            // should output 22
  cout << calVolume_stack(b, 12) << endl;      // should output 22

  cout << calVolume(c, 12) << endl;            // should output 25
  cout << calVolume_stack(c, 12) << endl;      // should output 25
  return 0;
}


// time: O(n), spacd: O(1)
int calVolume(int* land, int length) {
  int leftMax = 0;
  int rightMax = 0;

  int left = 0;
  int right = length - 1;

  int volume = 0;

  while(left < right) {
    if(land[left] > leftMax)
      leftMax = land[left];
    if(land[right] > rightMax)
      rightMax = land[right];
    if(leftMax >= rightMax)
      volume += rightMax - land[right--];
    else
      volume += leftMax  - land[left++];
  }
  return volume;
}


// time: O(n), space: O(n)
int calVolume_stack(int* land, int length) {
  stack<pair<int, int> > s;
  int water = 0;

  for (int i = 0; i < length; i++) {
    int height = 0;
    
    while(!s.empty()) {
      int bar = s.top().first;
      int pos = s.top().second;

        /*
         *                      -------------- <- land[i]
  bar -> * ---------            --------------
         * ----------------------------------- <- height
         * -----------------------------------
         *         |<- width ->|
         *
         * width = i - pos - 1
         */

      water += (min(bar, land[i]) - height) * (i - pos - 1);
      height = bar;

      if(land[i] < bar)
        break;
      else
        s.pop();
    }

    s.push(make_pair(land[i], i));
  }
  return water;
}
