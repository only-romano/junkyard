#include <stdio.h>
#include <stdlib.h>

void arrOnly();
void arrOnly2();
void arrMezo();

int main(void)
{
    arrOnly();
    arrOnly2();
    arrMezo();
    return 0;
}

void arrOnly()
{
    int a[] = {1, 2, 3, 4, 5};

    for (int i = 0; i < 5; i++)
    {
        printf("a[%d]: address = %p \t value = %d\n", i, a+i, *(a+i));
    }
    printf("\n");
}

void arrOnly2()
{
    char a[5] = {'A', 'B', 'C', 'D', 'E'};

    for (char *ptr = a; ptr <= &a[4]; ptr++)
    {
        printf("address = %p \t value = %c\n", ptr, *ptr);
    }
    printf("\n");
}

void arrMezo()
{
    int a[3][4] = { {1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12} };
    int n = sizeof(a) / sizeof(a[0]);
    int m = sizeof(a[0]) / sizeof(a[0][0]);

    printf("%d, %d, %d\n\n", n, m, sizeof(a[0]));

    int *final  = a[0] + n*m - 1;
    for (int *ptr = a[0], i = 0; i < m*n;)
    {
        printf("%d\t", *ptr++);
        if (++i % m == 0)
        {
            printf("\n");
        }
    }
}
