#include "iostream"
#include "vector"
#include "map"
#include "BSTStructure.h"
using namespace std;

void print(node* root);
void printHelp(node*, map<int, vector<int> >&, int);

int main()
{
  node* n1 = makeBST(1, NULL, NULL);
  node* n3 = makeBST(3, NULL, NULL);
  node* n2 = makeBST(2, n1, n3);
  print(n2);
  return 0;
}

void print(node* root) {
  map<int, vector<int> > m;
  int currDist = 0;
  printHelp(root, m, currDist);

  map<int, vector<int> >::iterator it;
  for (it = m.begin(); it != m.end(); it++) {
    for (unsigned long i = 0; i < it->second.size(); ++i) {
      cout << it->second[i] << endl;
    }
  }
}

void printHelp(node* root, map<int, vector<int> >& m, int currDist) {
  if (root == NULL) {
    return;
  }

  m[currDist].push_back(root->val);
  printHelp(root->left, m, currDist - 1);
  printHelp(root->right, m, currDist + 1);
  return;
}
