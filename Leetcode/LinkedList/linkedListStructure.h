//==================================================
// This header file contains definition of different
// structure and correspoding helper function
//==================================================
#include <random>
using namespace std;

class node {
  public:
	int val;
	node *next;
  node *random;

  node() {}

  node(int val) {
    this->val = val;
    this->next = NULL;
    this->random = NULL;
  }

  node(int val, node* next) {
    this->val = val;
    this->next = next;
    this->random = NULL;
  }

  node(int val, node* next, node *random) {
    this->val = val;
    this->next = next;
    this->random = random;
  }
};

void deleteNode(node *head) {
	if(head == NULL)
		return;
	deleteNode(head->next);
	delete head;
}

void printNodeHelp(node* head) {
	if(head == NULL)
		return;
  cout << head->val;
  if(head->random != NULL)
    cout << "[" << head->random->val << "]";
  if(head->next == NULL) {
    cout << endl;
    return;
  }
  cout << ", ";
  printNodeHelp(head->next);
}

void printNode(node* head) {
  if(head == NULL)
    cout << "NULL POINTER" << endl;
  else
    printNodeHelp(head);
}

int getLength(node* head) {
  int len = 0;
  while(head) {
    len++;
    head = head->next;
  }
  return len;
}

int getLength(node* head, node*& tail) {
  int len = 0;
  tail = NULL;
  while(head) {
    len++;
    tail = head;
    head = head->next;
  }
  return len;
}

node* genListHelp(int m, int n) {
  if(n == 0)
    return NULL;
  return new node(m - n, genListHelp(m, n - 1));
}

node* genList(int n) {
  return genListHelp(n, n);
}

void reverseLinkedlist(node*& head){
  if(head == NULL || head->next == NULL)
    return;

  node* newhead = NULL;
  while(head) {
    node* next = head->next;
    head->next = newhead;
    newhead = head;
    head = next;
  }

  head = newhead;
}
