#include <iostream>
#include <vector>
#include <queue>
using namespace std;

/*
 * Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.
*/

struct compare {
  bool operator()(const int& l, const int& r) {
    return l > r;
  }
};

// with heap, complexity O(nlogK)
void kSort_heap(vector<int>& a, int k) {
  priority_queue<int, vector<int>, compare> heap;   // our min heap
  
  for(int i = 0; i <= k; i++) {
    heap.push(a[i]);
  }

  for(int i = k + 1, j = 0; j < (int)a.size(); i++, j++) {
    a[j] = heap.top();
    heap.pop();

    if(i < (int)a.size())
      heap.push(a[i]);
  }
}


// without extra space, complexity: O(nK)
void kSort_intertion(vector<int>& a) {
  int i, key, j;
  for (i = 0; i < (int)a.size(); ++i) {
    key = a[i];
    j = i - 1;

    /* Move elements of a[0..i-1], that are greater than key, to one postition ahead of their
     * current position
     * This loop will run at most k times
     */
    while(j >= 0 && a[j] > key) {
      a[j+1] = a[j];
      j--;
    }
    a[j+1] = key;
  }
}

int main()
{
  vector<int> a = {2, 6, 3, 12, 56, 8};
  //kSort_heap(a, 3);
  kSort_intertion(a);
  //for(int i = 0; i < (int)a.size(); i++) {
    //cout << a[i] << endl;
  //}
  return 0;
}
