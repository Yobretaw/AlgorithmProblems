#include <iostream>
#include <vector>
using namespace std;

void solve_help( vector<vector<char> > &board, int x, int y, int** path) {
	path[x][y] = 1;
	if( board[x][y] == 'X' ) return;
	if( board[x][y] == 'O' ) board[x][y] = 'Y';

	if( x > 0 )
		if( !path[x-1][y] )
		       	solve_help( board, x-1, y, path );
	if( x < board.size()-1)
		if( !path[x+1][y] )
			solve_help( board, x+1, y, path );
	if( y > 0 )
		if(!path[x][y-1])
			solve_help(board, x, y-1, path);
	if( y < board[0].size()-1 )
		if(!path[x][y+1])
			solve_help(board, x, y+1, path);
}

void solve( vector<vector<char> > &board ) {
	
	if( board.size() <= 2 )
		return;
	
	int row = board.size();
	int col = board[0].size();

	int** path = new int*[row];
	for( int i = 0; i < row; i++ )
		path[i] = new int[col];
	for( int i = 0; i < row; i++ )
		for( int j = 0; j < col; j++ )
			path[i][j] = 0;

	for( int i = 0; i < row; i++ ) {
		if( board[i][0] == 'O' )
			solve_help(board, i, 0, path);
		if( board[i][col-1] == 'O' )
			solve_help(board, i, col-1, path);
	}
	for( int j = 0; j < col; j++ ) {
		if( board[0][j] == 'O' )
			solve_help(board, 0, j, path);
		if( board[row-1][j] == 'O' )
			solve_help(board, row-1, j, path);
	}

	for( int i = 0; i < row; i++ ) {
		for( int j = 0; j < col; j++ ) {
			//cout << (board[i][j] == 'Y');
			//board[i][j] = (board[i][j]=='Y')?'O':'X';
			if( board[i][j] == 'Y' )
				board[i][j] = 'O';
			else if( board[i][j] == 'O' )
				board[i][j] = 'X';
		}
	}
}

int main() {
	vector<vector<char> > v(3,vector<char>(3));

	v[0].push_back('O');
	v[0].push_back('O');
	v[0].push_back('O');

	v[1].push_back('O');
	v[1].push_back('O');
	v[1].push_back('O');

	v[2].push_back('O');
	v[2].push_back('O');
	v[2].push_back('O');


	/*
	v[0].push_back('X');
	v[0].push_back('X');
	v[0].push_back('X');
	v[0].push_back('X');

	v[1].push_back('X');
	v[1].push_back('O');
	v[1].push_back('O');
	v[1].push_back('X');

	v[2].push_back('X');
	v[2].push_back('X');
	v[2].push_back('O');
	v[2].push_back('X');

	v[3].push_back('X');
	v[3].push_back('O');
	v[3].push_back('X');
	v[3].push_back('X');
	*/

	solve(v);

	for( int i = 0; i < v.size(); i++ ) {
		for( int j = 0; j < v[i].size(); j++ )
			cout << v[i][j];
		cout << endl;
	}
	return 0;
}
