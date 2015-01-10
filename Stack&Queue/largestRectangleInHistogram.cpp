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

/* Given n non-negative integers representing the histogram's
 * bar height where the width of each bar is 1, find the area
 * of largest rectangle in the histogram
 */
int getMaxArea(vector<int>& heights) {
  if(heights.size() == 0)
    return 0;

  if(heights.size() == 1)
    return heights[0];


  stack<int> s;
  heights.push_back(0);

  int i = 0;
  int max_area = 0;
  while(i < heights.size()) {
    // If this bar is higher than the bar on top of stack,
    // push it to stack
    if(s.empty() || heights[i] >= heights[s.top()])
      s.push(i++);

    // If this bar is lower than the top of stack, calculate
    // area of rectangle with stack top as the smallest (or 
    // minimum height) bar. 'i' is 'right index' for the top
    // and element before top in stack is 'left index'
    else {
      int tmp = s.top();
      s.pop();
      max_area = max(max_area, heights[tmp] * (s.empty() ? i : i - s.top() - 1));
    }
  }

  return max_area;
}

// Time: O(n^2)
int getMaxArea_naive(vector<int> heights) {
  if(heights.size() == 0)
    return 0;

  if(heights.size() == 1)
    return heights[0];

  int max_area = 0;
  for (int i = 0; i < heights.size(); ++i) {
    int curr_area = heights[i];

    int l = i - 1;
    while(l >= 0 && heights[l] >= heights[i]) {
      curr_area += heights[i];
      l--;
    }

    int h = i + 1;
    while(h < heights.size() && heights[h] >= heights[i]) {
      curr_area += heights[i];
      h++;
    }
    max_area = max(max_area, curr_area);
  }
  return max_area;
}

int main() {
  vector<int> ret = { 2, 1, 5, 6, 2, 3 };
  cout << getMaxArea(ret) << endl;
  return 0;
}
