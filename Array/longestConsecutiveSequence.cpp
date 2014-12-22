#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

/* Given an unsorted array of integers, find the length 
 * of the longest consecutive sequnece.
 * 
 * For exampel, given [100, 4, 200, 1, 3, 2], the longest 
 * consecutive sequnece is [1, 2, 3, 4]. Return length 4
 */

/*
 * Sort the given array first and then find the longest 
 * consecutive sequnece
 * 
 * time: O(nlogn)
 */
int lcs_sort(const vector<int>& A) {
  int start = 0;
  int end = 0;
  int maxstart = 0;
  int maxend = 0;

  vector<int> arr(A);
  sort(arr.begin(), arr.end());

  int len = arr.size();
  for(int i = 1; i < len; i++) {
    if(arr[i] - arr[i-1] == 1) {
      end++;

      if((end - start) > (maxend - maxstart)) {
        maxstart = start;
        maxend = end;
      }
    } else {
      start = i;
      end = i;
    }
  }

  return maxend - maxstart + 1;
}

int lcs_hash(const vector<int>& A) {
  unordered_map<int, int> m; 

  int len = A.size();
  for(int i = 0; i < len; i++) {
    int curr = A[i];

    if(m.count(curr) != 0)
      continue;

    if(m.count(curr - 1) != 0 && m.count(curr + 1) != 0) {
      // curr connects two sequneces, update the start of
      // the first sequnece and the second sequnece
      int start = m[curr - 1];
      int end = m[curr + 1];

      m[start] = end;
      m[end] = start;
    } else if(m.count(curr - 1) != 0) {
      // curr follows one sequnece, update the start
      // of the sequnece and append curr to the end
      // of sequnece and updates its value to 'start'
      int start = m[curr - 1];

      m[start] = curr;
      m[curr] = start;
    } else if(m.count(curr + 1) != 0) {
      // curr prepend one sequence, udpate the end
      // of the sequence and prepend curr to the front
      // of the sequence and update its value to 'end'
      int end = m[curr + 1];

      m[curr] = end;
      m[end] = curr;
    } else {
      // no adjacent value of curr appears in the sequence
      m[curr] = curr;
    }
  }

  int maxdiff = INT_MIN;
  auto it = m.begin();
  while(it != m.end()) {
    if((it->second - it->first + 1) > maxdiff) {
       maxdiff = it->second - it->first + 1;
    }
    it++;
  }

  return maxdiff;
}

int lcs_hash2(const vector<int>& A) {
  unordered_map<int, bool> m;

  // first store all numbers into table
  int len = A.size();
  for(int i = 0; i < len; i++) {
    m[A[i]] = true;
  }
  
  // for every number in the table, expand
  // to left and right, record the longest
  // expansion.
  int maxdiff = INT_MIN;
  auto it = m.begin();
  while(it != m.end()) {
    // already seen
    if(!it->second) {
      it++;
      continue;
    }
    
    int i = 1, count = 1;
    int curr = it->first;
    while(m.count(curr - i) != 0) {
      m[curr - i] = false;
      count++;
      i++;
    }
    
    i = 1;
    while(m.count(curr + i) != 0) {
       m[curr + i] = false;
       count++;
       i++;
    }

    if(count > maxdiff) {
      maxdiff = count;
    }

    m[curr] = false;
    it++;
  }

  return maxdiff;
}

int main() {
  vector<int> arr = {103, 4, 101, 200, 102, 1, 104, 3, 100, 2};
  //cout << lcs_sort(arr) << endl;
  //cout << lcs_hash(arr) << endl;
  cout << lcs_hash2(arr) << endl;
  return 0;
}
