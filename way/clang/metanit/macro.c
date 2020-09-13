#include <stdio.h>

#define HELLO printf("Hello World!\n")
#define FOR for(int i = 0; i < 4; i++)
#define print(a) printf("%d \n", a)
#define t int
#define swap(t, x, y) { t temp = x; x = y; y = temp; }
#define min(a, b) (a < b ? a : b)
#define print_int(n) printf(#n"=%d \n", n);
#define printic(a, b, c) printf("%d\n", a##b##c);
#define unite(a, b, c) a##b##c
#define N 22
#define DEBUG
#define BETA

int main(void)
{
    FOR HELLO;

    t x = 10;
    print(x);
    t y = 20;
    print(y);
    print(22);

    x = 4;
    y = 10;
    swap(t, x, y);
    printf("x = %d \t y = %d", x, y);

    x = 23;
    y = 14;
    t z = min(x, y);
    print_int(x);
    print_int(y);
    t number = 203;
    print_int(number);
    printf("\nmin = %d\n", z);

    printic(2, 81, 34);
    x = unite(2, 81, 34);
    print_int(x);

#if N==22
    print_int(N);
#elif N==24
    print_int(24);
#else
    printf("N is undefined\n");
#endif

#ifdef DEBUG
    printf("Debug mode\n");
#else
    printf("Production mode\n");
#endif

#if defined DEBUG && !defined BETA
    printf("debug mode; final version");
#elif defined DEBUG && defined BETA
    printf("debug mode; beta version");
#else
    printf("undefined mode");
#endif

    return 0;
}
