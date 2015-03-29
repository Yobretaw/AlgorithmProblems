#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
#include "linkedListStructure.h"
using namespace std;

/* Given a linked list and a value x, partition it such that all nodes less
 * that x come before nodes greater than or equal to x
 *
 * You should preserve the original relative order of the nodes in each of
 * the two partition.
 *
 * For example, given 1->4->3->2->5->2 and x = 3, return 1->2->2->4->3->5
 */
node* partition(node* head, int x) {
  if(head == NULL || head->next == NULL)
    return head;

  node dummyl(-1, NULL);
  node dummyr(-1, NULL);

  node* left = &dummyl;
  node* right = &dummyr;

  for(node *curr = head; curr != NULL; curr = curr->next) {
    if(curr->val < x) {
      left->next = curr;
      left = curr;
    } else {
      right->next = curr;
      right = curr;
    }
  }
  
  left->next = dummyr.next;
  right->next = NULL;

  return dummyl.next;
}

int main() {
  node* l = new node(1, new node(6, new node(2, new node(5, new node(3, 0)))));
  printNode(l);
  l = partition(l, 3);
  printNode(l);
  return 0;
}
