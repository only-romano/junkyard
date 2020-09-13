#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 9; i++)
        printf("%d x %d = %d\n", i, i, i*i);
    printf("\n");

    for (int i = 1; i < 10; i++)
    {
        for (int j = 1; j < 10; j++)
            printf("%d \t", i*j);
        printf("\n");
    }
    printf("\n");

    int i = 6;
    do
    {
        printf("%d\t", i);
        i--;
    }
    while (i > 0);
    printf("\n");

    i = -1;
    do
    {
        printf("%d\t", i);
        i--;
    }
    while (i > 0);
    printf("\n");

    i = 6;
    while (i > 0)
    {
        printf("%d\t", i);
        i--;
    }
    printf("\n\n");

    i = 1;
    for (;;)
    {
        printf("%d x %d = %d\n", i, i, i*i);
        i++;
        if (i > 10) break;
    }
    printf("\n");

    int result = 0;
    for (int i = 0; i < 10; i++)
    {
        if (i % 2 == 0) continue;
        result += i;
    }
    printf("result = %d", result);

    return 0;
}
