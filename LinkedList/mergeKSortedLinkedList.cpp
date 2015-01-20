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

node *mergeSort(node *head) {
  if(head == NULL || head->next == NULL) return head;

  node *fast = head, *slow = head;
  while(fast->next != NULL && fast->next->next != NULL) {
    fast = fast->next->next;
    slow = slow->next;
  }

  fast = slow;
  slow = slow->next;
  fast->next = NULL;

  node *first = mergeSort(head);
  node *second = mergeSort(slow);
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
  node *head = new node(5, new node(4, new node(3, new node(2, new node(1, new node(0, NULL))))));
  printNode(mergeSort(head));
  return 0;
}
