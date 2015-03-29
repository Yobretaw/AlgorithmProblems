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

/*
 *  Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
 *  
 *  For example,
 *  Given the following matrix:
 *  
 *  [
 *   [ 1, 2, 3 ],
 *   [ 4, 5, 6 ],
 *   [ 7, 8, 9 ]
 *  ]
 *  
 *  You should return [1,2,3,6,9,8,7,4,5].
 */
vector<int> spiral(const vector<vector<int> >& mtx) {
  if(mtx.size() == 0) return vector<int>();

  int m = mtx.size();
  int n = mtx[0].size();

  vector<int> result(m * n);
  int idx = 0;
  int beginX = 0, endX = n - 1;
  int beginY = 0, endY = m - 1;
  while(true) {
    for(int i = beginX; i <= endX; ++i) result[idx++] = mtx[beginY][i];

    if(++beginY > endY) break;
    for(int i = beginY; i <= endY; ++i) result[idx++] = mtx[i][endX];

    if(beginX > --endX) break;
    for(int i = endX; i >= beginX; --i) result[idx++] = mtx[endY][i];

    if(beginY > --endY) break;
    for(int i = endY; i >= beginY; --i) result[idx++] = mtx[i][beginX];

    if(++beginX > endX) break;
  }
  return result;
}

/*
 *  Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
 *  
 *  For example,
 *  Given n = 3,
 *  
 *  You should return the following matrix:
 *  [
 *   [ 1, 2, 3 ],
 *   [ 8, 9, 4 ],
 *   [ 7, 6, 5 ]
 *  ]
 */
vector<vector<int> > generateSpiralMatrix(int n) {
  if(n == 0)
    return vector<vector<int> >();

  vector<vector<int> > mtx(n, vector<int>(n, 0));
  int begin = 0, end = n - 1;
  int num = 1;
  while(begin < end) {
     for(int i = begin; i < end; ++i) mtx[begin][i] = num++;
     for(int i = begin; i < end; ++i) mtx[i][end] = num++;
     for(int i = end; i > begin; --i) mtx[end][i] = num++;
     for(int i = end; i > begin; --i) mtx[i][begin] = num++;

     begin++;
     end--;
  }
  if(begin == end) mtx[begin][begin] = num;
  return mtx;
}


int main() {
  //vector<vector<int> > mtx = {
  //  { 1, 2, 3 },
  //  { 4, 5, 6 },
  //  { 7, 8, 9}
  //};

  vector<vector<int> > mtx = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12},
    {13, 14, 15, 16}
  };
  vector<int> result = spiral(mtx);
  for(auto val : result) cout << val << " ";
  return 0;
}
