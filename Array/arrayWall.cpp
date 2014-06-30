/*
 * Given a array of integers where each entry represents the height of the wall
 * Now imagine it rains. How much water is going to be accumulated in puddles 
 * between walls?
 */
#include "iostream"
using namespace std;

int calVolume(int* land, int length);

int main()
{
  int a[9] = {2, 5, 1, 2, 3, 4, 7, 7, 6};
  cout << calVolume(a, 9) << endl;
  return 0;
}


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
