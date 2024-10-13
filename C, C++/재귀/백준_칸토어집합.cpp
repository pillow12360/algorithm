#include <iostream>
#include <cmath>
using namespace std;

void cantor(int n) {
	int size = pow(3, n - 1); // size�� 3�� n-1 �������� �ʱ�ȭ

	// N = 0 �� ���
    // base ���̽�
	if (n == 0) {
		cout << "-";
		return;
	}

	// N��° ĭ��� ���� = N -1 ��° ĭ��� ������ 2�� ���� ��
	// ���̿� ������ N - 1��° ĭ��� ������ �����ŭ �־�� ��
	cantor(n - 1);

	for (int i = 0; i < size; i++) {
		cout << " ";
	} // ���� ����
	cantor(n - 1);

}

int main() {
	int N;
    // ������ cin ����
    // cin�� ���������� Ȯ�� �� while �� �ݺ�
	while (cin >> N) {
		cantor(N);
		cout << "\n";
	}

	return 0;
}