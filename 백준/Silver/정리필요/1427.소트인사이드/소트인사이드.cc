#include <string>
#include <iostream>
#include <vector>
using namespace std;

int main() {
	string str;
	cin >> str;
	vector<int> num(10, 0);
	
	for (int i = 0; i < str.size(); i++) { // str을 순회하며 각 숫자의 갯수를 기록
		int index = str[i] - '0';
		num[index]++;
	}
	for (int i = 9; i > -1; i--) { // 기록한 숫자만큼 9부터 갯수만큼 출력
		while (num[i] > 0) {
			cout << i;
			num[i]--;
		}
	}

	return 0;
}