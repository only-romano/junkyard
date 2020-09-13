#include <stdio.h>

int main(void)
{
    int numbers[4];
    numbers[0] = 1;
    numbers[1] = 2;
    numbers[2] = 3;
    numbers[3] = 4;
    printf("numbers[2] = %d\n", numbers[2]);

    int numb [] = { 10, 12, 13, 54, 43 };
    for (int i = 0; i < 5; i++)
    {
        printf("numb[%d] = %d\n", i, numb[i]);
    }
    printf("\n");

    int meznumb[][2] = { {1, 2}, {4, 5}, {7, 8} };
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            printf("meznumb[%d][%d] = %d\n", i, j, meznumb[i][j]);
        }
    }
    printf("\n");

    char welcome[] = "Hello";
    printf("Hello symbols: ");
    for (int i = 0; i < 6; i++)
    {
        printf(" %d(%c) ", welcome[i], welcome[i]);
    }

    return 0;
}
