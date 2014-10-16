#include <iostream>
#include <queue>
using namespace std;

// return true if left is larger than right
struct compare {
  bool operator()(const int& l, const int& r) {
    return l > r;
  }
};

int main() {
  priority_queue<int, vector<int>, compare> pq;

  // check if queue is empty
  cout << pq.empty() << endl;

  // pop up the top one
  cout << pq.pop() << endl;

  if(!pq.empty()) {
    // return the minimum value in the queue
    cout << pq.top() << endl;

    // pop the min value in the queue
    pq.pop();
  }
}


// priority_queue of pointers
struct compare_node {
  bool operator() (const node* l, const node* r) const {
    return l->val() < r->val();
  }
};

int main() {
  priority_queue<node*, vector<node*>, compare_node> pq;

  pq.push(new node(10, NULL, NULL));
}
