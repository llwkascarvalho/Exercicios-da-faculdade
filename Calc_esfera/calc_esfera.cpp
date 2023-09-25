#include <iostream>
#include <cmath>
#include <locale.h>

using namespace std;

const double PI = 3.14159265359;

void calc_esfera(float R, float *area, float *volume) {
    *area = 4.0 * PI * R * R;
    *volume = (4.0 / 3.0) * PI * R * R * R;
}

int main() {
    setlocale (LC_ALL,"portuguese");

    float raio, area, volume;

    cout << "Digite o raio da esfera: ";
    cin >> raio;

    calc_esfera(raio, &area, &volume);

    cout << "Área da superfície da esfera: " << area << endl;
    cout << "Volume da esfera: " << volume << endl;

    return 0;
}
