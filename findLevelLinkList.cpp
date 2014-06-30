#include <iostream>
#include "BSTStructure.h"
#include <vector>
using namespace std;

struct list{
	node *val;
	list *next;
};

list* makelist(node *val, list *next) {
	list *newlist = new list;
	newlist->val = val;
	newlist->next = next;
	return newlist;
}

void findLevelLinkList(node *root, int level, vector<list*>& v) {
	if (root == NULL)
		return;

	if(v.size() <= level) {
		list *newlist = makelist(root, NULL);
		v.push_back(newlist);
		findLevelLinkList(root->left, level + 1, v);
		findLevelLinkList(root->right, level + 1, v);
		return;
	}

	list *newlist = new list;
	newlist->val = root;
	newlist->next = v[level];
	v[level] = newlist;
	findLevelLinkList(root->left, level + 1, v);
	findLevelLinkList(root->right, level + 1, v);
}

vector<list*> find(node *root) {
	vector<list*> v;// = new vector<list*>;
	findLevelLinkList(root, 0, v);
	return v;
}

int main() {
	node *n1 = makeBST(1, NULL, NULL);
	node *n3 = makeBST(3, NULL, NULL);
	node *n2 = makeBST(2, n1, n3);
	node *n4 = makeBST(4, NULL, NULL);
	node *n6 = makeBST(6, NULL, NULL);
	node *n5 = makeBST(5, n4, n6);
	node *root = makeBST(10, n2, n5);
	vector<list*> v = find(root);
	for(int i = 0; i < v.size(); i++ ) {
		list* head = v[i];
		while(head != NULL) {
			cout << head->val->val << " ";
			head = head->next;
		}
		cout << endl;
	}
	return 0;
}
