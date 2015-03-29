#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
#include <utility>
using namespace std;

/* Determine the minimum number of meeting rooms to hold all meetings
 *
 * Example: input (1, 4), (2, 3), (3, 4), (4, 5)
 *          output: 2
 */
bool pairLess_first(const double& a, const double& b) {
  return a < b;
}

/* return ture if the x is of the from m.0 */
bool isEnd(double x) {
  double intpart;
  return modf(x, &intpart) == 0.0;
}

int minMeetingRoom(vector<pair<int, int> >& list) {
  int len = list.size();
  vector<double> dlist(2 * len, 0);
  
  for(int i = 0; i < len; ++i) {
    dlist[2 * i] = 1.0 * list[i].first + 0.1;
    dlist[2 * i + 1] = 1.0 * list[i].second;
  }

  // sort pairs based on starting time
  sort(dlist.begin(), dlist.end(), pairLess_first);

  int room = 0;
  int minroom = 0;
  for(int i = 0; i < 2 * len; ++i) {
    minroom = max(minroom, isEnd(dlist[i]) ? --room : ++room);
  }

  return minroom;
}

int main() {
  vector<pair<int, int> > list = {
    make_pair(1, 4),
    make_pair(4, 5),
    make_pair(3, 4),
    make_pair(2, 3),
    make_pair(1, 3)
  };

  cout << minMeetingRoom(list) << endl;
  return 0;
}
