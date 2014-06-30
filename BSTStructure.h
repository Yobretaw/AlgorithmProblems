struct node {
	int val;
	node *left;
	node *right;
};

node *makeBST(int val, node *left, node *right) {
	node *ret = new node;
	ret->val = val;
	ret->left = left;
	ret->right = right;
	return ret;
}

void printBST(node *root) {
	if(root == NULL)
		return;
	printBST(root->left);
	std::cout << root->val << " ";
	printBST(root->right);
}
