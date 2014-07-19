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

int main()
{
  node* head = new node(1, new node(2, new node(3, NULL)));
  reverse(head);
  printNode(head);
  return 0;
}
