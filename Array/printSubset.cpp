#include <iostream>
#include <vector>
using namespace std;

void printHelp(vector<int> v, int idx, vector<int>& store);

void printSubset(vector<int> v) {
  vector<int> store;
  printHelp(v, 0, store);
}


void printHelp(vector<int> v, int idx, vector<int>& store) {
  for(int i = idx; i < v.size(); i++) {
    store.push_back(v[i]);

    for(int i = 0; i < store.size(); i++) {
      cout << store[i];
    }

    cout << endl;

    printHelp(v, i+1, store);
    store.pop_back();
  }
}


int main(){
  vector<int> v;
  for(int i = 0; i < 3; i++)
    v.push_back(i);

  vector<int> store;
  printSubset(v);
  return 0;
}
