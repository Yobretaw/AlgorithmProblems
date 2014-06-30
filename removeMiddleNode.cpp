//======================================================
// Implemen an algorithm to delete a ndoe in the middle
// of a single linked list, given only access to that node
//======================================================

#include <iostream>
#include "linkedListStructure.h"
using namespace std;

// Simply copy the data from the next node into this node
// and then delete next node
void removeMiddleNode(node * mid) {
	node *nextNode = mid->next;
	mid->val = nextNode->val;
	mid->next = nextNode->next;
	delete nextNode;
}

int main() {
	node *head = makenode(1, NULL);
	node *n2 = makenode(2, NULL);
	node *n3 = makenode(3, NULL);
	node *n4 = makenode(4, NULL);
	node *n5 = makenode(5, NULL);

	head->next = n2;
	n2->next = n3;
	n3->next = n4;
	n4->next = n5;

	printNode(head);
	cout << endl;
	removeMiddleNode(n3);
	printNode(head);
}
