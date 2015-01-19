#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
#include "linkedListStructure.h"
using namespace std;

node *mergeHelp(node *a, node *b);
node *mergeRecursion(const vector<node*>& list, int start, int end);

node *merge(const vector<node*>& list) {
  if(list.size() == 0) return NULL;
  return mergeRecursion(list, 0, list.size() - 1);
}

node *mergeRecursion(const vector<node*>& list, int start, int end) {
  if(start == end)
    return list[start];

  int mid = (end - start) / 2 + start;
  node *first = mergeRecursion(list, start, mid);
  node *second = mergeRecursion(list, mid + 1, end);

  return mergeHelp(first, second);
}

node *mergeHelp(node *a, node *b) {
  node dummy(-1, NULL);
  node *p = &dummy;
  while(a != NULL || b != NULL) {
    int val1 = a == NULL ? INT_MAX : a->val;
    int val2 = b == NULL ? INT_MAX : b->val;
    if(val1 <= val2) {
      p->next = a;
      a = a->next;
    } else {
      p->next = b;
      b = b->next;
    }
    p = p->next;
  }
  return dummy.next;
}

int main() {
  return 0;
}
