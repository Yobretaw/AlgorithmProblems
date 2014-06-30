#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include "BSTStructure.h"
using namespace std;

bool inorderSuccessor(node* root, node* a, node*& result);
node* findLeftmostNode(node* root);

int main(int argc, const char *argv[])
{
    node* result = NULL;

    node* n1 = makeBST(1, NULL, NULL);
    node* n3 = makeBST(3, NULL, NULL);
    node* n2 = makeBST(2, n1, n3);

    node* n5 = makeBST(5, NULL, NULL);
    node* n7 = makeBST(7, NULL, NULL);
    node* n6 = makeBST(6, n5, n7);

    node* n4 = makeBST(4, n2, n6);

    node* n10 = makeBST(10, NULL, NULL);
    node* n9 = makeBST(9, n4, n10);

    inorderSuccessor(n9, n7, result);
    cout << result->val << endl;
    return 0;
}


bool inorderSuccessor(node* root, node* a, node*& result) {
    if (root == NULL) {
        return false;
    }

    if (root->val == a->val) {
        if (root->right != NULL) {
            result = findLeftmostNode(root->right);
        }

        // no right subTree, require parent node handle this case
        return true;
    }

    if (inorderSuccessor(root->left, a, result)) {
        if (result == NULL) {
            result = root;
        }
        return true;
    } else {
        return inorderSuccessor(root->right, a, result);
    }
}

node* findLeftmostNode(node* root) {
    if (root->left == NULL) {
        return root;
    }

    return findLeftmostNode(root->left);
}
