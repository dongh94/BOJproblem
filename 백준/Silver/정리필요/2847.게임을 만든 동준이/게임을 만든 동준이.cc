#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	int scores[n];

	for (int i = 0; i < n; i++) {
		cin >> scores[i];
	}

	int count = 0;
	for (int i = n-1; i >= 1; i--) {		
		while (scores[i-1] >= scores[i]) {
			scores[i-1]--;
			count++;
		}
	}
	
	cout << count << endl;

	return 0;
}