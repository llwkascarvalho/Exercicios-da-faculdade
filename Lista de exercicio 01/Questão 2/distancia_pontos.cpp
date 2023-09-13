#include <iostream>
#include <locale.h>
#include <cmath>

using namespace std;

void calculo(){

    int x1,x2,y1,y2;

    cout << "Digite X1: ";
    cin >> x1;
    cout << "Digite Y1: ";
    cin >> y1;
    cout << "Digite X2: ";
    cin >> x2;
    cout << "Digite Y2: ";
    cin >> y2;
    double distancia = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    cout << "Distância: " << distancia;
}

int main(){

    setlocale(LC_ALL, "portuguese");
    
    calculo();

    return 0;
}