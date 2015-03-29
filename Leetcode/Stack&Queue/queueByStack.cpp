#include "iostream"
#include "stack"
using namespace std;

template <class T>class myQueue {
  stack<T> a;
  stack<T> b;

public:
  void push(T val) {
    if(a.size() == 0) {
      a.push(val);
    } else {
      transit(a, b);
      a.push(val);
      transit(b, a);
    }
  }

  void pop() {
    a.pop();
  }

  T peek() {
    return a.top();
  }

  T remove() {
    T val = a.top();
    a.pop();
    return val;
  }

  void transit(stack<T>& from, stack<T>& to) {
    while(from.size() != 0) {
      to.push(from.top());
      from.pop();
    }
  }
};

int main()
{
  myQueue<int>* q = new myQueue<int>();
  int count = 10;
  for(int i = 0; i < count; i++) {
    q->push(i);
  }

  for(int i = 0; i < count; i++) {
    cout << q->remove()  << endl;
  }

  return 0;
}
