//=======================================================
// delete the duplicate node in a linked list without using
// buffer 
//
// Runtime: O(n^2)
//=======================================================
#include <iostream>
#include "linkedListStructure.h"
using namespace std;

void removeDuplicate(node* head) {
	if(head == NULL)
		return;
	while(head->next != NULL) {
		int val = head->val;
		node *prev = head;
		node *nextNode = head->next;

		while(nextNode != NULL) {
			if(nextNode->val == val) {
				prev->next = nextNode->next;
				node *nodeToBeDeleted = nextNode;
				nextNode = prev->next;
				delete nodeToBeDeleted;
				continue;
			}
			prev = prev->next;
			nextNode = nextNode->next;
		}
		head = head->next;
	}
}
