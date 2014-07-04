#include <iostream>
#include <linkedListStructure.h>
using namespace std;

void removeOdd(node*& head) {
  for(node** curr = &head; *curr; ) {
    node* entry = *curr;
    if(curr->val % 2 == 1) {
      *curr = entry->next;
      delete entry;
    } else {
      *curr = &(entry->next);
    }
  }
}

int main() {
  node* a = makenode(1, makenode(2, makenode(3, makenode(4, makenode(5, makenode(6, NULL))))));
  removeOdd(a);
  printNode(a);
  deleteNode(a);
}
