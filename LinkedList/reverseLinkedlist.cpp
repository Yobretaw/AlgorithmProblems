#include "iostream"
#include "linkedListStructure.h"
using namespace std;

void reverse(node*& head){
  if(head == NULL || head->next == NULL)
    return;

  node* newhead = NULL;
  while(head) {
    node* next = head->next;
    head->next = newhead;
    newhead = head;
    head = next;
  }

  head = newhead;
}


/* Reverse a linked list from position m to n. Do it 
 * in-place and in one-pass.
 *
 * For example: Given 1->2->3->4->5, m = 2 and n = 4
 * return 1->4->3->2->5
 *
 * Note: 1 <= m <= n <= length of list
 */
node* partialReverse(node* head, int m, int n) {
  node dummy(0, head);

  node* head2 = &dummy;
  for(int i = 0; i < m - 1; ++i)
    head2 = head2->next;

  node* tail = head2->next;
  node* curr = tail->next;

  for(int i = m; i < n; ++i) {
    tail->next = curr->next;
    curr->next = head2->next;
    head2->next = curr;
    curr = tail->next;
  }

  return dummy.next;
}


int main()
{
  node* head = new node(1, new node(2, new node(3, new node(4, new node(5, NULL)))));
  //reverse(head);
  node* rev = partialReverse(head, 1, 4);
  //printNode(head);
  printNode(rev);
  return 0;
}
