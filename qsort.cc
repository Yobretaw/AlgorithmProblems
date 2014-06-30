#include <iostream>
using namespace std;

int partition(int* list, int p, int r) {
	int pivot = list[r];	

	while(p < r) {
		while(list[p] < pivot)
			p++;
		while(list[r] > pivot)
			r--;
		if(list[p] == list[r])
			p++;
		else if(p < r){
			int temp = list[r];
			list[r] = list[p];
			list[p] = temp;
		}
	}

	return r;
}

void quicksort(int *list, int p, int r) {
	if(p < r) {
		int j = partition(list, p, r);
		quicksort(list, p, j - 1);
		quicksort(list, j + 1, r);
	}
}

int main() {
	int size = 1000000;
	int list[size];

	for(int i = 0; i < size; i++) {
		list[i] = size - i;
	}

	quicksort(list, 0, size - 1);

	for(int i = 0; i < size; i++) {
		cout << list[i] << endl;
	}

	return 0;
}
