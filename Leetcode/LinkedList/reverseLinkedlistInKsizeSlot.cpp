#include "iostream"
#include "linkedListStructure.h"
using namespace std;

node* getPrev(node* head, int k) {
  while(head != NULL && k != 1) {
    head = head->next;
    k--;
  }

  return head;
}

/* Givne a linked list, reverse the nodes of a linked list at a time
 * and return its modified list
 *
 * If the number of nodes is not mutiple of k then left-out nodes in
 * the ends should remain as it is
 *
 * You may NOT alter the values in the nodes, only nodes itself may
 * be changed
 */
node* reverse(node* head, int k) {
  if(head == NULL)
    return NULL;

  node* preNext = getPrev(head, k);
  if(preNext == NULL)
    return head;

  node *newhead = reverse(preNext->next, k);
  preNext->next = NULL;

  while(head != NULL) {
    node* next = head->next;
    head->next = newhead;
    newhead = head;
    head = next;
  }

  return newhead;
}

int main()
{
  node *head = genList(10);
  printNode(head);
  node* rev = reverse(head, 4);
  printNode(rev);
  return 0;
}
