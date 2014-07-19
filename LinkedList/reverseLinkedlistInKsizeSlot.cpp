#include "iostream"
#include "linkedListStructure.h"
using namespace std;

node* getPreNextNode(node* head, int k) {
  while(head != NULL && k != 1) {
    head = head->next;
    k--;
  }

  return head;
}

node* reverse(node* head, int k) {
  if(head == NULL)
    return NULL;

  node* preNext = getPreNextNode(head, k);
  node* next = NULL;

  if(preNext != NULL) {
    next = preNext->next;
    preNext->next = NULL;
  }

  node* rest = reverse(next, k);

  node* newhead = rest;
  while(head) {
    node* next = head->next;
    head->next = newhead;
    newhead = head;
    head = next;
  }

  return newhead;
}

int main()
{
  node* head = new node(11, NULL);
  node* cp = head;
  int count = 10;

  while(count != 0) {
    cp->next = new node(count, NULL);
    cp= cp->next;
    count--;
  }

  printNode(head);
  node* rev = reverse(head, 3);
  printNode(rev);
  return 0;
}
