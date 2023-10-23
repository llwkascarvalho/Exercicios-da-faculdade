#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>

using namespace std;

int findMax(const vector<int>& vetor, int left, int right) {
    if (left == right) {
        return vetor[left];
    }

    int mid = left + (right - left) / 2;
    int maxLeft = findMax(vetor, left, mid);
    int maxRight = findMax(vetor, mid + 1, right);

    return max(maxLeft, maxRight);
}

int main() {
    const int tamanho = 1000000;
    vector<int> vetor(tamanho);

    srand(static_cast<unsigned>(time(nullptr)));
    for (int i = 0; i < tamanho; ++i) {
        vetor[i] = rand();
    }

    int maior = findMax(vetor, 0, tamanho - 1);

    cout << "O maior numero no vetor: " << maior << endl;
    return 0;
}