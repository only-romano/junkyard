#include <stdio.h>

int main(void)
{
    short a = -2 > 5;
    short b = 0 < 7;
    short c = 0 == 0;
    short d = a && b || c;
    short e = -2 > 5 && 0 < 7 || 0 == 0;
    printf("a, b, c, d, e  -  %d, %d, %d, %d, %d\n", a, b, c, d, e);
}
