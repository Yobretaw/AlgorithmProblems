#include "iostream"
#include "string"
using namespace std;

void hanoi(int diskSize, int source, int dest, int spare) {
  if(diskSize == 0) {
    cout << "Move disk " << diskSize << " from " << source << " to " << dest << endl;
    return;
  }

  hanoi(diskSize - 1, source, spare, dest);
  cout << "Move disk " << diskSize << " from " << source << " to " << dest << endl;
  hanoi(diskSize - 1, spare, dest, source);
}

int main()
{
  hanoi(10, 1, 2, 3);
  return 0;
}
