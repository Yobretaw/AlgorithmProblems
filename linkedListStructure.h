//==================================================
// This header file contains definition of different
// structure and correspoding helper function
//==================================================

struct node {
	int val;
	node *next;
};

node* makenode(int val, node *next) {
	node *ret = new node;
	ret->val = val;
	ret->next = next;
	return ret;
}

void deleteNode(node *head) {
	if(head == NULL)
		return;
	deleteNode(head->next);
	delete head;
}

void printNode(node* head) {
	if(head == NULL)
		return;
	std::cout << head->val << " ";
	printNode(head->next);
}
