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

/* ****************************************************************************
 * 
 *  Given a collection of intervals, merge all overlapping intervals.
 *  
 *  For example, given [1,3],[2,6],[8,10],[15,18], return [1,6],[8,10],[15,18].
 *  
 * ****************************************************************************/
struct Interval {
  int start;
  int end;
  Interval(): start(0), end(0) {}
  Interval(int s, int e) : start(s), end(e) {}
};

bool compare(const Interval& l, const Interval& r) {
  return l.start < r.start;
}

vector<Interval> mergeInterval(vector<Interval>& intervals) {
  int n = intervals.size();

  if(n == 0 || n == 1) return intervals;
  sort(intervals.begin(), intervals.end(), compare);

  int i = 0;
  while(i < intervals.size() - 1) {
    if(intervals[i].end >= intervals[i + 1].start) {
      intervals[i].end = intervals[i + 1].end;
      intervals.erase(intervals.begin() + i + 1, intervals.begin() + i + 2);
    } else i++;
  }
  return intervals;
}

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

vector<Interval> mergeInterval2(vector<Interval>& intervals) {
   vector<Interval> newinterval;
   for(auto interval : intervals)
     newinterval = insert(newinterval, interval);
   return newinterval;
}

int main() {
  vector<Interval> intervals = {
    Interval(1, 3),
    Interval(2, 6),
    Interval(8, 10),
    Interval(15, 18)
  };
  vector<Interval> result = mergeInterval(intervals);
  for (int i = 0; i < result.size(); ++i) {
    cout << result[i].start << " " << result[i].end << endl;
  }
  return 0;
}
