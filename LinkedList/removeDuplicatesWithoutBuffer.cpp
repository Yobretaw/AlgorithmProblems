#include "iostream"
#include "linkedListStructure.h"
using namespace std;

void remove(node* head) {
  if(head == NULL || head->next == NULL) {
    return;
  }

  int val;
  node *pre, *curr;
  while(head) {
    val = head->val;
    pre = head;
    curr = head->next;

    while(curr) {
      if(curr->val == val) {
        pre->next = curr->next;
        delete curr;
        curr = pre->next;
      } else {
        pre = curr;
        curr = curr->next;
      }
    }
    head = head->next;
  }
}

int main()
{
  node* head = new node(1, new node(2, new node(1, new node(3, new node(3, new node(4, new node(4, NULL)))))));
  remove(head);
  printNode(head);
  return 0;
}
