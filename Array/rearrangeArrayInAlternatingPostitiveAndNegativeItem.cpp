#include "iostream"
#include "vector"
#include "queue"
using namespace std;

/* 
 * Given an array of positive and negative numbers, arrange them in an alternate fashion such that every negative number is followed by positive and vice-versa maintaining the order of appearance.
 
 * Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.
*/

// use extra space O(n), time complexity O(n)
void rearrange(vector<int>& a){
  queue<int> neg;
  queue<int> pos;

  for(int i = 0; i < (int)a.size(); i++) {
    if(a[i] >= 0)
      pos.push(a[i]);
    else
      neg.push(a[i]);
  }

  int idx = 0;
  while(!pos.empty() && !neg.empty()) {
    if(idx % 2 == 0) {
      a[idx] = pos.front();
      pos.pop();
    } else {
      a[idx] = neg.front();
      neg.pop();
    }

    idx++;
  }

  if(pos.empty() && neg.empty())
    return;

  queue<int> *rest = pos.empty() ? &neg : &pos;
  while(!rest->empty()) {
    a[idx++] = rest->front();
    rest->pop();
  }
}

void shift(vector<int>& a, int start, int end) {
  int tmp = a[end];
  while(end > start) {
    a[end] = a[end - 1];
    end--;
  }
  a[start] = tmp;
}

int findNext(vector<int>& a, int start, int sign) {
  while(start < (int)a.size()) {
    if((sign > 0 && a[start] * sign >= 0) ||
        (sign < 0 && a[start] * sign > 0))
      return start;
    start++;
  }

  return -1;
}

// time complexity: O(n^2)
void rearrange_inplace(vector<int>& a) {
  for(int i = 0; i < (int)a.size(); i++) {
    if((i % 2 == 0 && a[i] < 0) ||
        (i % 2 == 1 && a[i] > 0)) {
      int sign = -a[i];
      int nextPos = findNext(a, i + 1, sign);
      if(nextPos == -1)
        break;

      shift(a, i, nextPos);
    }
  }
}

int main()
{
  vector<int> a = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8};
  vector<int> b = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8};
  rearrange(a);
  rearrange_inplace(b);
  for(int i = 0; i < (int)a.size(); i++) 
    cout << a[i] << " " << b[i] << endl;

  return 0;
}
