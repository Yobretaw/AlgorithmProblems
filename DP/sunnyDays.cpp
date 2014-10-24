#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;


// we have one day activities and two day activities, and given a list
// of weather status for the next x days, find the max number of sunny 
// days that can be used to host the activities
//
// w is the list of weather for the next x days
// 0 represents rainny day, and 1 represents sunny day
int arrange(const vector<int>& w, int oneDay, int twoDay, int threeDay) {
  int count = 0;
  vector<int> past(w.size());
  for(int i = 0; i < 3 && i < w.size(); i++) {
    count += w[i];
    past[i] = count;
  }

  int days = oneDay + 2 * twoDay + 3 * threeDay;
  if(days <= count) { 
    return days;
  } else if(w.size() < 3) {
    return count;
  }


  for (int i = 3; i < w.size(); i++) {
    cout << (i - 1) << ": " << past[i - 1] << endl;
    if(w[i] == 0) {
      past[i] = past[i-1];
      continue;
    }

    int toThisDay = 0;
    int sunCount = 0;   // today is sunny day

    for(int j = i; j >= i - 2; j--) {
      sunCount += w[j];
      toThisDay = max(toThisDay, past[j-1] + sunCount);
    }

    past[i] = toThisDay;
  }

  if(past[past.size() - 1] >= days)
    return days;
  else
    return past[past.size() - 1];
}

int main()
{
  vector<int> w = {1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1};
  cout << arrange(w, 1, 1, 2) << endl;
  return 0;
}
