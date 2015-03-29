#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include "linkedListStructure.h"
#include <unordered_map>
using namespace std;

/* Given a linked list, swap every two adjacents ndoes and return
 * its head
 * 
 * For example: given 1->2->3->4, return 2->1->4->3
 * 
 * Your algorithm should use only constant space. You may NOT modify
 * the values in the list, only nodes itself can be changed.
 */
node* swapPairs(node* head) {
  if(head == NULL || head->next == NULL)
    return head;

  node dummy(0, head);
  node *prev = &dummy;
  node *curr = prev->next;
  node *temp;

  while(curr != NULL && curr->next != NULL) {
    prev->next = curr->next;
    temp = curr->next->next;
    curr->next->next = curr;
    prev = curr;
    curr = temp;
  }

  prev->next = curr;
  return dummy.next;
}

node* swapPairsRecursion(node *head) {
  if(head == NULL || head->next == NULL)
    return head;

  node *next = head->next;
  node *temp = next->next;
  next->next = head;
  head->next = swapPairsRecursion(temp);

  return next;
}

int main() {
  node *l = genList(10);
  printNode(l);
  l = swapPairs(l);
  printNode(l);
  l = swapPairsRecursion(l);
  printNode(l);
  return 0;
}
