#include <stdio.h>

int main(void)
{
    int a = 2 << 2;
    int b = 16 >> 3;
    int c = 5 | 2;
    printf("2 << 2 = %d\n16 >> 3 = %d\n5 | 2 = %d\n", a, b, c);
    a = 6 & 2;
    b = 6 ^ 2;
    c = ~9;
    printf("6 & 2 = %d\n6 ^ 2 = %d\n~9 = %d\n", a, b, c);

    a = 5; printf("%d; ", a); a += 10; printf("%d; ", a);
    a -= 3; printf("%d; ", a); a *= 2; printf("%d; ", a);
    a /= 6; printf("%d; ", a); a <<= 4; printf("%d; ", a);
    a >>= 2; printf("%d.", a);

    return 0;
}
