#include <iostream>
#include <stdio.h>
#include "linkedListStructure.h"
using namespace std;

void removeOdd(node*& head);

int main()
{
  node* a = makenode(1, makenode(2, makenode(3, makenode(4, makenode(5, NULL)))));
  removeOdd(a);
  printNode(a);
  return 0;
}

/*
void removeOdd(node*& head) {
  for (node** curr = &head; *curr; ) {
    node* entry = *curr;
    if (entry->val % 2 == 1) {
      *curr = entry->next;
      delete entry;
    } else {
      curr = &entry->next;
    }
  }
}
*/

void removeOdd(node*& head) {
  node** curr = &head;
  while(*curr) {
    node* entry = *curr;
    if (entry->val % 2 == 1) {
      *curr = entry->next;
      delete entry;
    } else {
      curr = &entry->next;
    }
  }
}
