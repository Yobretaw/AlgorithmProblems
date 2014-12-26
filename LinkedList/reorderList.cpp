#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include "linkedListStructure.h"
#include <unordered_map>
using namespace std;

void reverse(node*& head) {
  if(head == NULL || head->next == NULL)
    return;

  node *newhead = NULL;
  node *curr = head;
  while(curr != NULL) {
    node* tmp = curr->next;
    curr->next = newhead;
    newhead = curr;
    curr = tmp;
  }

  head = newhead;
}

//=======================================================
//                    Reorder List
//=======================================================
// Given a singly linked list L: L0->L1->L2->L3->...->Ln-1->Ln
// reordr it to: L0->Ln->L1->Ln-1->...
// 
// You must do this in-place
// 
// Example:
// Input:  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
// Output: {0, 9, 1, 8, 2, 7, 3, 6, 4, 5}
node* reorder(node *head) {
  if(head == NULL || head->next == NULL)
    return head;

  node dummy(0, head);
  node *prev = &dummy;
  node *fast = head, *slow = head;
  while(fast != NULL && fast->next != NULL) {
    fast = fast->next->next;
    slow = slow->next;
    prev = prev->next;
  }

  prev->next = NULL;
  reverse(slow);

  while(head->next != NULL) {
    node *next = slow->next;
    slow->next = head->next;
    head->next = slow;
    head = slow->next;
    slow = next;
  }

  head->next = slow;
  return dummy.next;
}

int main() {
  node *l = genList(10);
  printNode(l);
  //reverse(l);
  l = reorder(l);
  printNode(l);
  //reorder(l);
  return 0;
}
