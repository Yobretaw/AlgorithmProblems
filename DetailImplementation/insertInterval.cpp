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
 *  Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
 *  
 *  You may assume that the intervals were initially sorted according to their start times.
 *  
 *  Example 1:
 *  Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
 *  
 *  Example 2:
 *  Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
 *  
 *  This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
 */
struct Interval {
  int start;
  int end;
  Interval(): start(0), end(0) {}
  Interval(int s, int e) : start(s), end(e) {}
};

vector<Interval> insert(vector<Interval>& intervals, Interval newinterval) {
  int n = intervals.size();
  int start = newinterval.start;
  int end = newinterval.end;

  if(n == 0) return vector<Interval>{newinterval};
  if(intervals[0].start > end) {
    intervals.insert(intervals.begin(), newinterval);
    return intervals;
  } else if(intervals[n - 1].end < start) {
    intervals.push_back(newinterval);
    return intervals;
  }

  int startIdx = -1, endIdx = -1;
  for (int i = 0; i < n; ++i) {
    if(intervals[i].end >= start && startIdx == -1)
      startIdx = i;
    if(intervals[i].start <= end)
      endIdx = i;
  }
  Interval itv(min(intervals[startIdx].start, start), max(intervals[endIdx].end, end));
  intervals.erase(intervals.begin() + startIdx, intervals.begin() + endIdx + 1);
  intervals.insert(intervals.begin() + startIdx, itv);
  return intervals;
}

int main() {
  vector<Interval> intervals = {
    Interval(1, 2),
    Interval(3, 5),
    Interval(6, 7),
    Interval(8, 10),
    Interval(12, 16)
  };
  vector<Interval> result = insert(intervals, Interval(2, 8));
  for (int i = 0; i < result.size(); ++i) {
    cout << result[i].start << " " << result[i].end << endl;
  }
  return 0;
}
