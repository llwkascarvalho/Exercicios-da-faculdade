#include <iostream>
#include <stdio.h>

using namespace std;

int main (){

    setlocale (LC_ALL,"portuguese");
    
    int L, termo1 = 1, termo2 = 1;

    cout << "Digite um valor inteiro positivo L: ";
    cin >> L;

    if (L >= 1) {
        cout << termo1 << endl;
    }

    if (L >= 2) {
        cout << termo2 << endl;
    }

    int proximo_termo = termo1 + termo2;
    
    while (proximo_termo <= L) {
        cout << proximo_termo << endl;
        termo1 = termo2;
        termo2 = proximo_termo;
        proximo_termo = termo1 + termo2;
    }

    cout << endl;

    return 0;
}