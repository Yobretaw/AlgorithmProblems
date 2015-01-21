#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
using namespace std;

#define BITPERWORD 32
#define SHIFT 5
#define MASK 0x1F

class Bitmap {
  public:
    Bitmap(int n) {
      a = new int(n / BITPERWORD + 1);
      capacity = n;
    }

    void set(int n) {
      if(n < 0 || n > capacity) return;
      a[n >> SHIFT] |= (1 << (n & MASK));
    }

    void clr(int n) {
      a[n >> SHIFT] &= ~(1 << (n & MASK));
    }

    bool test(int n) {
      if(n < 0 || n > capacity) return 0;
      return a[n >> SHIFT] & (1 << (n & MASK));
    }

    ~Bitmap() {
      delete a;
    }

  private:
    int capacity;
    int* a;
};

int main() {
  Bitmap *a = new Bitmap(100);
  for(int i = 0; i < 100; ++i) {
    if(i % 2 == 0) a->set(i);
  }
  for(int i = 0; i < 100; ++i) {
    cout << a->test(i) << endl;
  }
  return 0;
}
