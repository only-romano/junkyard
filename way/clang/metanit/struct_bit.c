#include <stdio.h>

struct point
{
    unsigned int x:5;
    unsigned int y:3;
};

union code
{
    struct point p;
    struct {
        unsigned a0:1;
        unsigned a1:1;
        unsigned a2:1;
        unsigned a3:1;
        unsigned a4:1;
        unsigned a5:1;
        unsigned a6:1;
        unsigned a7:1;
    } byte;
};

int main(void)
{
    struct point center = { 0, 5 };
    center.x = 2;
    printf("x = %d \t y = %d\n", center.x, center.y);

    union code c;
    c.p = center;
    printf("7 \t 6 \t 5 \t 4 \t 3 \t 2 \t 1 \t 0\n");
    printf("%d \t %d \t %d \t %d \t %d \t %d \t %d \t %d\n",
        c.byte.a7, c.byte.a6, c.byte.a5, c.byte.a4,
        c.byte.a3, c.byte.a2, c.byte.a1, c.byte.a0);

    return 0;
}