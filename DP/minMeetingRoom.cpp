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
bool pairLess(const pair<double, double>& a, const pair<double, double>& b) {
  return a.first < b.first;
}

bool pairLessL(const double& a, const double& b) {
  return a < b;
}

bool isInt(double x) {
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
  sort(dlist.begin(), dlist.end(), pairLessL);

  int room = 0;
  int minroom = 0;
  for(int i = 0; i < 2 * len; ++i) {
    if(isInt(dlist[i]))
      room++;
    else
      room--;
    
    if(room > minroom)
      minroom = room;
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
