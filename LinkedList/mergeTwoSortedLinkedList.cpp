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

node *merge(node *a, node *b) {
  if(a == NULL && b == NULL)
    return NULL;

  if(a == NULL || b == NULL)
    return a == NULL ? b : a;

  node dummy = node(-1, NULL);
  node *head = &dummy;
  while(a != NULL && b != NULL) {
    head->next = a->val < b->val ? a : b;
    head = head->next;

    if(a->val < b->val) a = a->next;
    else b = b->next;
  }

  if(a == NULL && b == NULL)
    return dummy.next;

  if(a == NULL || b == NULL)
    head->next = a == NULL ? b : a;

  return dummy.next;
}

int main() {
  //node* a = new node(1, new node(2, new node(3, new node(3, new node(4, new node(4, new node(5, NULL)))))));
  //node* b = new node(1, new node(2, new node(3, new node(3, new node(4, new node(4, new node(5, NULL)))))));

  node* a = new node(1, NULL);
  node* b = NULL;
  printNode(merge(a, b));
  return 0;
}
