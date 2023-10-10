#include <iostream>
#include <vector>

using namespace std;

bool subsetSum(vector<int>& V, int target) {
    int n = V.size();
    
    // Caso base: se o alvo é 0, encontramos uma solução vazia
    if (target == 0) {
        return true;
    }
    
    // Caso base: se não há mais elementos no vetor, não podemos encontrar uma solução
    if (n == 0) {
        return false;
    }
    
    // Ignorar o último elemento e verificar se é possível encontrar uma solução
    // excluindo-o
    if (V[n - 1] > target) {
        return subsetSum(V, target);
    }
    
    // Tentar incluir ou excluir o último elemento e verificar se é possível encontrar
    // uma solução
    return subsetSum(V, target) || subsetSum(V, target - V[n - 1]);
}

int main() {
    vector<int> V = {1, 10, 5, 2, 10, 20};
    int target = 12;
    
    if (subsetSum(V, target)) {
        cout << "É possível encontrar um subconjunto cuja soma é igual a " << target << endl;
    } else {
        cout << "Não é possível encontrar um subconjunto cuja soma é igual a " << target << endl;
    }
    
    return 0;
}
