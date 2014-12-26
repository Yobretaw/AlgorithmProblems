#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include "linkedListStructure.h"
#include <unordered_map>
using namespace std;

//==========================================================
//                Linked List Cycle I
//==========================================================
/* Given a linked list, determine if it has a cycle in in
 * 
 * Follow up: Can you solve it without using extra space ?
 */
bool hasCycle(node *head) {
  node *slow = head, *faster = head;

  while(faster != NULL && faster->next != NULL) {
    faster = faster->next->next;
    slow = slow->next;
    if(faster == slow) return true;
  }

  return false;
}


//==========================================================
//                Linked List Cycle I
//==========================================================
/* Given a linked list, return the node where the cycle begins.
 * If there is no cycle, return NULL.
 */
node* findEntry(node *head) {
  node *slow = head, *faster = head;
  while(faster != NULL && faster->next != NULL) {
    faster = faster->next->next;
    slow = slow->next;

    // meet
    if(faster == slow) {
      node* slow2 = head;
      while(slow2 != slow) {
        slow = slow->next;
        slow2 = slow2->next;
      }

      return slow;
    }
  }

  return NULL;
}

int main() {
  node *l = genList(2);
  printNode(findEntry(l));
  return 0;
}
