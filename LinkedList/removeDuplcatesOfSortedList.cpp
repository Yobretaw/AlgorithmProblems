#include "iostream"
#include "linkedListStructure.h"
using namespace std;

struct compare {
  bool operator()(const node*& l, const node*& r) {
    return l->val > r->val;
  }
};

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

int main()
{
  node* head = new node(1, new node(1, new node(2, new node(2, new node(3, new node(4, new node(4, new node(5, new node(5, NULL)))))))));
  remove(head);
  printNode(head);
  return 0;
}
