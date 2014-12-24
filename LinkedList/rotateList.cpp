#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
#include "linkedlistStructure.h"
using namespace std;

/* Given a list, rotate the list to the right by k places, where k is
 * non negative
 * 
 * For example: 1->2->3->4->5 and k = 2, return 4->5->1->2->3
 */
node* rotateList(node* head, int k) {
  node* tail;

  if(head == NULL
      || head->next == NULL
      || (k %= getLength(head, tail)) == 0)
    return head;

  node dummy(0, head);
  node *newhead = head;
  node *prev = &dummy;

  while(k > 0) {
    prev = prev->next;
    k--;
  }
  
  prev->next = NULL;
  tail->next = head;
  return newhead;
}

int main() {
  int len = 10;
  node *l = genList(len);
  for(int i = 0; i < len; ++i)
    printNode(l = rotateList(l, 1));

  return 0;
}
