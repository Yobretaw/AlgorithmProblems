#include "iostream"
#include "BSTStructure.h"
using namespace std;

void findHelp(node* root, int curr, int& max, string path, string& maxPath) {
  if(root == NULL)
    return;

  curr += root->val;
  path += path == ""? "" : ", ";

  stringstream ss;
  ss << root->val;
  path += ss.str();
  if(root->left == NULL && root->right == NULL && curr > max) {
    max = curr;
    maxPath = path;
  }

  findHelp(root->left, curr, max, path, maxPath);
  findHelp(root->right, curr, max, path, maxPath);
}

string findPath(node* root) {
  int max = 0;
  string path = "";
  findHelp(root, 0, max, "", path);

  return path;
}

int main()
{
  node* root = new node(7, 
      new node(3, 
        new node(1, 
          new node(0, NULL, NULL),
          new node(2, NULL, NULL)),
        new node(5,
          new node(4, NULL, NULL),
          new node(6, NULL, NULL))),
      new node(11,
        new node(9,
          new node(8, NULL, NULL),
          new node(10, NULL, NULL)),
        new node(13,
          new node(12, NULL, NULL),
          new node(14, NULL, NULL))));

  printBST(root);
  cout << findPath(root) << endl;
  return 0;
}
