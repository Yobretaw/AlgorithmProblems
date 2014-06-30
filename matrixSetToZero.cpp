//=====================================================
// Write an algorithm such that if an element in an MxN
// matrix is 0, its entire row and column is set to 0
// 
// Runtime: O(MN)
//=====================================================

#include <iostream>
#include <stdlib.h>
using namespace std;

void setZero(int **matrix, int numRow, int numCol) {
	int *row = new int[numRow];
	int *col = new int[numCol];
	
	// store the row and column index with value 0
	for(int i = 0; i < numRow; i++) {
		for(int j = 0; j < numCol; j++) {
			if(matrix[i][j] == 0) {
				row[i] = 1;
				col[j] = 1;
			}
		}
	}

	// Set matrix[i][j] to 0 if either row i or column j has 0
	for(int i = 0; i < numRow; i++) {
		for(int j = 0; j < numCol; j++) {
			if(row[i] == 1 || col[j] == 1) {
				matrix[i][j] = 0;
			}
		}
	}
	delete [] row;
	delete [] col;
}

int main() {
	int size = 20;
	int **m = new int*[size];
	for(int i = 0; i < size; i++) {
		m[i] = new int[size];
	}
	for(int i = 0; i < size; i++)
		for(int j = 0; j < size; j++)
			m[i][j] = 1;

	m[4][4] = 0;
	m[10][10] = 0;
	setZero(m, size, size);

	for(int i = 0; i < size; i++) {
		for(int j = 0; j < size; j++)
			cout << m[i][j] << " ";
		cout << endl;
	}
}
