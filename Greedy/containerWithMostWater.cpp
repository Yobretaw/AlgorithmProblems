#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
using namespace std;

/*
 * Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that
 * the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container
 * contains the most water.
 * 
 * Note: You may not slant the container.
 */
// native algorithm. Time O(n^2), space O(1)
int findContainer(const vector<int>& points) {
  int n = points.size();
  if(n < 2) return 0;
  
  int maxvolume = 0;
  for (int left = 0; left < n - 1; ++left)
    for(int right = left + 1; right < n; ++right)
      maxvolume = max(maxvolume, (right - left) * min(points[left], points[right]));

  return maxvolume;
}

// greedy algorithm. Time O(n), space O(1)
int findContainer2(const vector<int>& points) {
  int n = points.size();
  if(n < 2) return 0;

  int start = 0, end = n - 1;
  int result = 0;
  while(start < end) {
    result = max(result, (end - start) * min(points[start], points[end]));
    if(points[start] < points[end]) start++;
    else end--;
  }
  return result;
}

int main() {
  vector<int> points = {3, 2, 1, 5, 4, 6, 2};
  cout << findContainer(points) << endl;
  cout << findContainer2(points) << endl;
  return 0;
}
