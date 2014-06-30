#include <iostream>
#include "linkedListStructure.h"
using namespace std;

node *reverse(node *head);

int main() {
	//node *head = makenode(1, makenode(2, makenode(3, makenode(4, NULL))));
  node* head = makenode(1, makenode(2, NULL));
	node *new_head = reverse(head);

	printNode(new_head);
	cout << endl;
	deleteNode(head);
}

node *reverse(node *head) {
	node *new_head = NULL;

	while(head) {
		node *next = head->next;    // record next node
		head->next = new_head;      // make current next node to the previous head
		new_head = head;            // refresh new_head
		head = next;                // refresh head
	}

	return new_head;
}
