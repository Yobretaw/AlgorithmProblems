#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
#include "graphStructure.h"
using namespace std;

/*
 *  Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
 *  
 *  
 *  OJ's undirected graph serialization:
 *  Nodes are labeled uniquely.
 *  
 *  We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
 *  As an example, consider the serialized graph {0,1,2#1,2#2,2}.
 *  
 *  The graph has a total of three nodes, and therefore contains three parts as separated by #.
 *  
 *    1. First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
 *    2. Second node is labeled as 1. Connect node 1 to node 2.
 *    3. Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
 *
 *  Visually, the graph looks like the following:
 *  
 *       1
 *      / \
 *     /   \
 *    0 --- 2
 *         / \
 *         \_/
 */
UndirectedGraphNode* cloneHelp(UndirectedGraphNode* g, unordered_map<UndirectedGraphNode*, UndirectedGraphNode*>& seen) {
  int label = g->label;
  if(seen.count(g)) return seen[g];

  UndirectedGraphNode* gg = new UndirectedGraphNode(label);
  seen[g] = gg;
  for(auto neighbor : g->neighbors) {
    UndirectedGraphNode* tmp = cloneHelp(neighbor, seen);
    gg->neighbors.push_back(tmp);
  }
  return gg;
}

UndirectedGraphNode* cloneGraph(UndirectedGraphNode* g) {
  if(g == NULL) return g;
  unordered_map<UndirectedGraphNode*, UndirectedGraphNode*> seen;
  return cloneHelp(g, seen);
}

int main() {
  UndirectedGraphNode* g = new UndirectedGraphNode(0);
  g->neighbors.push_back(g);
  g->neighbors.push_back(g);
  UndirectedGraphNode* gg = cloneGraph(g);
  return 0;
}
