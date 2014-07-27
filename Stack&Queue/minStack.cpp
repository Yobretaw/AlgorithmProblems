#include "iostream"
#include "stack"
using namespace std;

class minStack {
  stack<int> s;
  stack<int> ms;

public:
  void push(int item) {
    if(s.size() == 0 || (s.size() != 0 && ms.top() >= item)) {
      ms.push(item);
    }

    s.push(item);
  }

  void pop() {
    if(ms.top() == s.top())
      ms.pop();

    s.pop();
  }

  int min() {
    return ms.top();
  }
};

int main()
{
  minStack* ms = new minStack();
  ms->push(5);
  ms->push(4);
  ms->push(3);
  ms->push(2);
  ms->push(1);
  ms->push(0);
  ms->push(1);
  ms->push(2);
  ms->push(3);
  ms->push(4);
  ms->push(5);

  for(int i = 0; i < 11; i++) {
    cout << ms->min() << endl;
    ms->pop();
  }
  return 0;
}
