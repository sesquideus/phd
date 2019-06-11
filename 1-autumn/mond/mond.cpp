#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

long double e = 0.95;
long double mu = 100;
long double L = 10;

int main() {
    long double df = 1e-5;
    long double u = 1;
    long double du = 0;
    long double ddu = 0;

    for (int i = 0; i*df < 500; ++i) {
        ddu = (1/(1+e)) * (1 - exp(-mu)) / (1 - exp(-mu*u)) - u;
        du += ddu * df;
        u += du * df;
        if (i % 1000 == 0) printf("%8.2Lf %20.15Lf\n", i*df, u);
    }

}
