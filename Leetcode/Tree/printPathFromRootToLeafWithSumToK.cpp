#include "iostream"
#include "vector"
#include "BSTStructure.h"
using namespace std;

void print(node* root, vector<int>& path, int sum) {
  if(root == NULL)
    return;

  if(root->left == NULL && root->right == NULL) {
    if(sum - root->val == 0) {
      for(int i = 0; i < (int)path.size(); i++)
        cout << path[i] << " ";
      cout << root->val << endl;
      return;
    }
  }

  path.push_back(root->val);
  print(root->left, path, sum - root->val);
  print(root->right, path, sum - root->val);
  path.pop_back();
}

int main()
{
  node* root = new node(-15,
      new node(5,
        new node(-8,
          new node(2, NULL, NULL),
          new node(6, new node(21, NULL, NULL), NULL)),
        new node(1, NULL, NULL)),
      new node(6, 
        new node(3, new node(15, NULL, NULL), NULL),
        new node(9, NULL,
          new node(0,
            new node(4, NULL, NULL),
            new node(-1, 
              new node(10, NULL, NULL),
              NULL)))));
  
  printBST(root);
  vector<int> path;
  print(root, path, 9);
  return 0;
}
