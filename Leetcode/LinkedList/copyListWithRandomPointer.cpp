#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include "linkedListStructure.h"
#include <unordered_map>
using namespace std;

/* A linked list is given such that each node contains an additional
 * random pointer which could point to any node in the list or null.
 * 
 * Return a deep copy of the list
 */
node* copyDeep(node* head) {
  if(head == NULL)
    return NULL;

  node *curr = head;
  while(curr) {
    curr->next = new node(curr->val, curr->next);
    curr = curr->next->next;
  }

  curr = head;
  while(curr) {
    if(curr->random != NULL)
      curr->next->random = curr->random->next;
    curr = curr->next->next;
  }

  node dummy(0, head);
  node *prev = &dummy;
  node *next;
  while(head != NULL) {
    next = head->next;
    head->next = next->next;
    prev->next = next;
    head = head->next;
    prev = prev->next;
  }

  return dummy.next;
}

int main() {
  node *l1 = new node(1, NULL);
  node *l2 = new node(2, NULL);

  l1->next = l2;
  l1->random = l2;
  l2->random = l1;

  printNode(copyDeep(l1));
  return 0;
}
