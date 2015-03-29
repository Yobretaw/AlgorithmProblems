#include <vector>
#include <unordered_map>
using namespace std;
struct UndirectedGraphNode {
  int label;
  std::vector<UndirectedGraphNode*> neighbors;
  
  // constructor
  UndirectedGraphNode(int x): label(x) {};

  public:

  void insertNeighbor(UndirectedGraphNode* g) {
    this.neighbors.push_back(g);
  }

  void clearNeighbor() {
    this.neighbors.clear();
  }

  void printHelp(UndirectedGraphNode* g, unordered_map<UndirectedGraphNode*, UndirectedGraphNode*> seen) {
    int label = g->label;
    cout << label << " " << endl;
  }

  void print() {
    unordered_map<UndirectedGraphNode*, UndirectedGraphNode*> seen;
    printHelp(this, seen);
  }
};
