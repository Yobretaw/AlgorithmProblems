#include "iostream"
#include "linkedListStructure.h"
using namespace std;

/* Given a sorted linked list, delete all duplicates such that
 * each element appear only once.
 */
void remove(node* head) {
  if(head == NULL || head->next == NULL)
    return;

  while(head) {
    int val = head->val;
    node** curr = &(head->next);

    while(*curr && (*curr)->val == val) {
      node* temp = *curr;
      *curr = temp->next;
      delete temp;
    }

    head = head->next;
  }
}

/* Given a sorted linked list, delete all nodes that have duplicates, leaving
 * only distinct numbers from original list
 *
 * Example: given 1->2->3->3->4->4->5, return 1->2->5
 */
node* removeAllDups(node* head) {
  if(head == NULL && head->next == NULL)
    return head;

  node dummy(head->val + 1, head);
  node* prev = &dummy;
  while(head != NULL && head->next != NULL) {
    bool hasDup = head->val == head->next->val;

    while(head->next != NULL && head->val == head->next->val) {
      node* tmp = head->next;
      head->next = head->next->next;
      delete tmp;
    }

    if(hasDup) {
      prev->next = head->next;
      delete head;
      head = prev->next;
    } else {
      prev = prev->next;
      head = head->next;
    }
  }

  return dummy.next;
}

int main()
{
  //node* head = new node(1, new node(1, new node(2, new node(2, new node(3, new node(4, new node(4, new node(5, new node(5, NULL)))))))));
  node* head = new node(1, new node(2, new node(3, new node(3, new node(4, new node(4, new node(5, NULL)))))));
  //remove(head);
  head = removeAllDups(head);
  printNode(head);
  return 0;
}
