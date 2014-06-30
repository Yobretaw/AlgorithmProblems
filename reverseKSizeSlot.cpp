#include "iostream"
#include "linkedListStructure.h"
using namespace std;

node* reverse(node*, int k);
node* getNext(node*, int k);

int main()
{
  node* a = makenode(1, makenode(2, makenode(3, makenode(4, NULL))));
  printNode(reverse(a, 2));
  return 0;
}

node* reverse(node* head, int k) {
  if (head == NULL) {
    return NULL;
  }
  
  node* pre = head;
  node* newHead = NULL;
  node* nextHead = getNext(head, k);
  while(head != NULL) {
    // reverse current segment of nodes
    node* next = head->next;
    head->next = newHead;
    newHead = head;
    head = next;
  }

  // reverse the rest, append head to tail
  pre->next = reverse(nextHead, k); 
  return newHead;
}

node* getNext(node* head, int k) {
  if(head == NULL) return NULL;
  
  node* pre = head;
  while(head != NULL && k > 0) {
    pre = head;
    head = head->next;
    k--;
  }
  pre->next = NULL;
  return head;
}

