#include <stdio.h>
#include <stdlib.h>

void mallocTry();
void mezoTry();

int main(void)
{
    int *block1, *block2;
    int *block3 = NULL;
    block1 = malloc(5 * sizeof(int));
    block2 = calloc(6, sizeof(int));
    block3 = realloc(block3, 7 * sizeof(int));

    free(block1);
    free(block2);
    free(block3);
    mallocTry();
    mezoTry();
    return 0;
}

void mallocTry()
{
    int *block;
    int n;

    printf("Size of array=");
    scanf("%d", &n);

    block = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
    {
        printf("block[%d] = ", i);
        scanf("%d", &block[i]);
    }
    printf("\n");

    for (int i = 0; i < n; i++)
    {
        printf("%d \t", block[i]);
    }
    printf("\n\n");

    free(block);
}

void mezoTry()
{
    int **table;
    int *rows = NULL;
    int rowscount, d;

    printf("Rows count = ");
    scanf("%d", &rowscount);

    table = calloc(rowscount, sizeof(int*));
    rows = realloc(rows, rowscount * sizeof(int));

    for (int i = 0; i < rowscount; i++)
    {
        printf("\nColumns count for row %d = ", i);
        scanf("%d", &rows[i]);
        table[i] = malloc(rows[i] * sizeof(int));

        for (int j = 0; j < rows[i]; j++)
        {
            printf("table[%d][%d] = ", i, j);
            scanf("%d", &d);
            table[i][j] = d;
        }
    }
    printf("\n");

    for (int i = 0; i < rowscount; i++)
    {
        printf("\n");

        for (int j = 0; j < rows[i]; j++)
        {
            printf("%d \t", table[i][j]);
        }
        free(table[i]);
    }

    free(table);
    free(rows);
}
