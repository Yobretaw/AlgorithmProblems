#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
#include "linkedListStructure.h"
using namespace std;

node* insertionSort(node* head) {
  if(head == NULL) return NULL;

  head->next = insertionSort(head->next);
  node dummy(head->val, head);
  head = &dummy;
  while(head->next != NULL && head->val >= head->next->val) {
    swap(head->val, head->next->val);
    head = head->next;
  }
  return dummy.next;
}

node *insertionSort2(node *head) {
  if(head == NULL) return NULL;
  node dummy(INT_MIN, NULL);
  node *prev, *next, *curr;
  while(head != NULL) {
    prev = &dummy;
    next = head->next;
    curr = prev->next;
    while(curr != NULL && curr->val < head->val) {
      prev = prev->next;
      curr = curr->next;
    }
    prev->next = head;
    head->next = curr;
    head = next;
  }
  return dummy.next;
}

int main() {
  node *head = new node(3, new node(4, new node(1, new node(2, new node(5, NULL)))));
  //node *head = new node(2, new node(1, new node(1, NULL)));
  printNode(insertionSort2(head));
  return 0;
}
