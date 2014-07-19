#include "iostream"
#include "linkedListStructure.h"
using namespace std;

void sort(node*& head) {
  if(head == NULL || head->next == NULL) {
    return;
  }

  node* pre = NULL;
  node* fast = head;

  // find the middle element of the list 
  while(fast != NULL && fast->next != NULL) {
    fast = fast->next->next;
    pre = (pre == NULL) ? head : pre->next;
  }

  node* mid = pre->next;
  pre->next = NULL;

  sort(head);
  sort(mid);

  node* newhead = NULL;
  if(head->val < mid->val) {
    newhead = head;
    head = head->next;
  } else {
    newhead = mid;
    mid = mid->next;
  }

  node* copy = newhead;
  while(head != NULL && mid != NULL) {
    copy->next = (head->val < mid->val) ? head : mid;
    copy = copy->next;

    if(copy == head) {
      head = head->next;
    } else {
      mid = mid->next;
    }
  }

  copy->next = (head == NULL) ? mid : head;
  head = newhead;
}

int main()
{
  int val;
  int len = 0;
  node* head;
  node* cp;
  while(cin >> val) {
    if(head == NULL) {
      head = new node(val, NULL);
      cp = head;
    } else {
      cp->next = new node(val, NULL);
      cp = cp->next;
    }
  }
  printNode(head);
  sort(head);
  printNode(head);
  return 0;
}
