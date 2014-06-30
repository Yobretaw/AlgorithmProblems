#include <iostream>
#include <vector>
#include "BSTStructure.h"
using namespace std;

bool findPath(node *, node *);

node *find(node *root, node *a, node *b)  {

    string val = "hello";

	if(root == NULL)
		return NULL;

	if(root == a || root == b)
		return root;

	node *l = find(root->left, a, b);
	node *r = find(root->right, a, b);

	if(l && r)
		return root;
	else if(l)
		return l;
	return r;
}


int main() {
	node *n3 = makeBST(3, NULL, NULL);
	node *n6 = makeBST(6, NULL, NULL);
	node *n9 = makeBST(9, NULL, NULL);
	node *n13 = makeBST(13, NULL, NULL);
	node *n17 = makeBST(17, NULL, NULL);
	node *n20 = makeBST(20, NULL, NULL);
	node *n4 = makeBST(4, n3, NULL);
	node *n8 = makeBST(8, n6, n9);
	node *n19 = makeBST(19, n17, n20);
	node *n5 = makeBST(5, n4, n8);
	node *n15 = makeBST(15, n13, n19);
	node *n10 = makeBST(10, n5, n15);

	node *common = find(n10, n6, n17);
	cout << common->val << endl;


	return 0;
}
