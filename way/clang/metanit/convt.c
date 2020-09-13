#include <stdio.h>

int main (void)
{
    char c = 6;
    int d = c;
    printf("char: %c; int: %d\n", c, d);

    int a = 10;
    double b = 4;
    double e = a + b;
    printf("a = %d; b = %3.2f; c = %3.2f\n", a, b, e);

    a = 10;
    d = 4;
    int f = a / d;
    double g = a / d;
    double h = (double)a / (double)d;
    printf("f = %d; g = %3.2f; h = %3.2f\n", f, g, h);

    int number = 70;
    char symbol = (char) number;
    printf("Symbol: %c\nSymbol (int code): %d\n", symbol, symbol);
}
