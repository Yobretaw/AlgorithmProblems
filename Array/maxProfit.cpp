#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

//==================================================================
//                         Max Profit
//==================================================================
/* Say you have an array for which the i-th element is the price of
 * given stock on day i. Design an algorithm to find the maximum
 * profit. You may complete AS MANY TRANSACTIONS AS you want
 *                         ------------------------
 *
 * Note: you may NOT engage in multiple trasactions at the same time
 * (i.e you must sell the stock before buying again)
 */
int maxProfit(const vector<int>& prices) {
  int profit = 0;
  int diff;
  for (int i = 1; i < (int)prices.size(); ++i) {
    diff = prices[i] - prices[i - 1];
    if(diff > 0)
      profit += diff;
  }
  return profit;
}

//==================================================================
//                        Max Profit I
//==================================================================
/* Say you have an array for which the i-th element is the price of
 * given stock on day i. Design an algorithm to find the maximum
 * profit. You may complete AT MOST ONE trasaction.
 *                         ------------
 *
 * Note: you may NOT engage in multiple trasactions at the same time
 * (i.e you must sell the stock before buying again)
 */
int maxProfit1(const vector<int>& prices) {
  int profit = 0;
  int low = INT_MAX;

  for (int i = 0; i < (int)prices.size(); ++i) {
    low = min(prices[i], low);

    if((prices[i] - low) > profit) {
      profit = prices[i] - low;
    }
  }

  return profit;
}

//==================================================================
//                        Max Profit II
//==================================================================
/* Say you have an array for which the i-th element is the price of
 * given stock on day i. Design an algorithm to find the maximum
 * profit. You may complete AT MOST TWO trasactions.
 *                         ------------
 *
 * Note: you may NOT engage in multiple trasactions at the same time
 * (i.e you must sell the stock before buying again)
 */
int maxProfit2(const vector<int>& prices) {
  const int len = prices.size();
  if(len < 2)
    return 0;

  // first[i] is the max profit in interval [0, i - 1]
  // second[i] is the max profit in interval [i, len - 1]
  vector<int> first(len, 0);
  vector<int> second(len, 0);

  int valley = prices[0];
  for (int i = 1; i < len; ++i) {
    valley = min(valley, prices[i]);
    first[i] = max(first[i - 1], prices[i] - valley);
  }

  int peak = prices[len - 1];
  for (int i = len - 2; i >= 0; --i) {
    peak = max(peak, prices[i]);
    second[i] = max(second[i], peak - prices[i]);
  }

  // the max_profit will be max(first[i] + second[i]) for
  // 0 <= i <= len - 1
  int max_profit = 0;
  for (int i = 0; i < len; ++i) {
    max_profit = max(max_profit, first[i] + second[i]);
  }

  return max_profit;
}

int main() {
  vector<int> p = {3, 2, 6, 5, 0, 3};
  //vector<int> p = {2, 1, 2, 0, 1};
  //vector<int> p = {1, 2, 4};
  //vector<int> p = {1, 4, 2};
  cout << maxProfit1(p) << endl;
  return 0;
}
