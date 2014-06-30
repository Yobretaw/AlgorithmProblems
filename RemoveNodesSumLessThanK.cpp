#include <iostream>
#include <string>
using namespace std;

struct node {
	int val;
	node *left;
	node *right;
};

void deleteNode(node*& root);
void printNode(node *root);
node* makeNode(int val, node *left, node *right);

node* remove(node* root, int k) {
	if(root == NULL)
		return NULL;
	if(root->val >= k)
		return root;
	else {
		node* left = remove(root->left, k - root->val);
		node* right = remove(root->right, k - root->val);
		root->left = left;
		root->right = right;
		if(!left && !right) {
			delete root;
			return NULL;
		}
		return root;
	}
}


int main() {
	
	node *n15 = makeNode(15, NULL, NULL);
	node *n13 = makeNode(13, NULL, NULL);
	node *n8 = makeNode(8, NULL, NULL);
	node *n12 = makeNode(12, NULL, NULL);
	node *n11 = makeNode(11, NULL, NULL);
	node *n6 = makeNode(6, NULL, NULL);
	node *n14 = makeNode(14, n15, NULL);
	node *n10 = makeNode(10, NULL, n11);
	node *n9 = makeNode(9, n13, n14);
	node *n4 = makeNode(4, n8, n9);
	node *n5 = makeNode(5, n12, NULL);
	node *n7 = makeNode(7, n10, NULL);
	node *n2 = makeNode(2, n4, n5);
	node *n3 = makeNode(3, n6, n7);
	node *n1 = makeNode(1, n2, n3);

	//remove(n1, 45);
	node* newnode = remove(n1, 45);
	printNode(newnode);

	return 0;
}

node* makeNode(int val, node *left, node *right) {
	node* retval = new node;
	retval->val = val;
	retval->left = left;
	retval->right = right;
	return retval;
}


void deleteNode(node*& root) {
	if(root == NULL)
		return;

	cout << root->val << endl;
	delete root;
	root = NULL;
}

void printNode(node *root) {
	if(root == NULL)
		return;
	cout << root->val << endl;
	printNode(root->left);
	printNode(root->right);
}
