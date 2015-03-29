#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

/* There are N gas stations along a circular route, where the amount of
 * gas at station i is gas[i].
 *
 * You have a car with unlimited gas tank and it cost cost[i] of gas to
 * travel from station i to station i+1. You begin the journey with an
 * empty at one of the gas stations.
 *
 * Return the starting gas station's index if you can travel around the
 * circuit once, otherwise return -1
 *
 * Note: The solution is guaranteed to be unique.
 */
/* 
 * Time: O(n), space: O(1)
 */
int canCompleteCircuit(const vector<int>& gas, const vector<int>& cost) {
  // 'total' is the total amount of gas accumulated from the first station
  // to current station. When loop exists, if total < 0 then the total
  // amount of gas is not enough for the car to traveral all N stations
  int total = 0;
  int sum = 0;
  int startIdx = -1;

  for (int i = 0; i < gas.size(); i++) {
    sum += gas[i] - cost[i];
    total += gas[i] - cost[i];

    if(sum < 0) {
      startIdx = i;
      sum = 0;
    }
  }

  return total >= 0 ? startIdx + 1: -1;
}

int main() {
  return 0;
}
