#include <stdio.h>

int main(void)
{
    int a = 67;
    int b = 33;
    int c = a + b + 7;
    printf("a + b + 7 = %d\n", c);
    c = a - b;
    printf("a - b = %d\n", c);
    c = a * b;
    printf("a * b = %d\n", c);
    c = a / b;
    printf("a / b = %d\n (int)", c);
    float d = a / b;
    printf("a / b = %3.2f\n (float with ints)", d);
    d = (float)a / (float)b;
    printf("a / b = %3.2f\n (float with floats)", d);
    c = a % b;
    printf("a % b = %d\n", c);
    c = a + 5 * b;
    printf("a + 5 * b = %d\n", c);
    c = (a + 5) * b;
    printf("(a + 5) * b = %d\n", c);
    a = 8;
    b = 7;
    c = a+++--b;
    printf("c = a+++--b\na (8) = %d; b (7) = %d; c = %d\n", a, b, c);

    return 0;
}
