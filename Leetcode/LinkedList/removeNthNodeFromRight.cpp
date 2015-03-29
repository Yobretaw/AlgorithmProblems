#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
#include "linkedlistStructure.h"
using namespace std;

node* remove(node* head, int n) {
  if(head == NULL)
    return head;

  // the reason to use dummy node is that we need to get the node
  // that comes before the nth node is the list in order to delete
  // the nth node.
  node dummy(0, head);
  node *faster = &dummy;
  node *slower = &dummy;

  for(int i = 0; i < n; ++i)
    faster = faster->next;

  while(faster->next != NULL) {
    faster = faster->next;
    slower = slower->next;
  }

  node *tmp = slower->next;
  slower->next = tmp->next;
  delete tmp;
  return dummy.next;
}

int main() {
  int n = 8;
  node *l = genList(n);
  for(int i = 0; i < n; ++i) {
    l = remove(l, 1);
    printNode(l);
  }
  return 0;
}
