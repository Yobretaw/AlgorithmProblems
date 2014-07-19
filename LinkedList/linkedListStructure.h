//==================================================
// This header file contains definition of different
// structure and correspoding helper function
//==================================================
using namespace std;

class node {
  public:
	int val;
	node *next;

  node() {}

  node(int val) {
    this->val = val;
    this->next = NULL;
  }

  node(int val, node* next) {
    this->val = val;
    this->next = next;
  }
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
  if(head->next == NULL) {
    cout << endl;
    return;
  }
	printNode(head->next);
}

int len(node* head) {
  int len = 0;
  while(head) {
    len++;
    head = head->next;
  }

  return len;
}
