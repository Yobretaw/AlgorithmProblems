#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
#include <algorithm>
#include <numeric>
using namespace std;

/* There are N children standing in a line. Each child is
 * assigned a rating value.
 * 
 * You are giving candies to these children subjected to
 * the following requirements:
 *
 *  - Each child must have at least one candy
 *  - Children with a higher rating get more candies than
 *    their neighbors
 *    
 *  Find the minimum amount of candies you must give.
 */
/* Time: O(n), space: O(n) */
int countCandy(const vector<int>& ratings) {
  int n = ratings.size();

  // init vector with value 1 since each child
  // must have at least one candy
  vector<int> increment(n, 1);

  // scan from left
  for(int i = 1; i < n; ++i)
    if(ratings[i] > ratings[i - 1])
      increment[i] = increment[i - 1] + 1;

  // scan from right
  for(int i = n - 2; i >= 0; i--)
    if(ratings[i] > ratings[i + 1])
      increment[i] = max(increment[i + 1] + 1, increment[i]);

  // count the total amount of candies needed
  int total = 0;
  for (int i = 0; i < n; ++i)
    total += increment[i];

  return total;
}

int main() {
  vector<int> ratings = {4, 2, 3, 4, 1};  // should be 9
  //vector<int> ratings = {1, 3, 2, 4, 2, 2, 1, 5}; // should be 12
  //vector<int> ratings;      // should be 55
  //for(int i = 0; i < 10; ++i)
    //ratings.push_back(i);
  cout << countCandy(ratings) << endl;
  return 0;
}
